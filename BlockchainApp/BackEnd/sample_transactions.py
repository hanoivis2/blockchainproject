import time
import requests
import json
from blockchain.transaction.wallet import Wallet
from blockchain.utils.helpers import BlockchainUtils


def post_transaction(sender_private_key, receiver_public_key, amount, type, port):
    url = "http://localhost:" + port + "/api/v1/transaction/create/"
    package = {
        "sender_private_key": sender_private_key,
        "receiver_public_key": receiver_public_key,
        "amount": amount,
        "type": type
    }
    response = requests.post(url, json=package, timeout=15)
    print(response.text)

def wallet_create(port):
    url = "http://localhost:" + port + "/api/v1/account/create/"
    response = requests.post(url, timeout=15)
    print(response.text)
    return response.text

def wallet_statistic(public_key, port):
    url = "http://localhost:" + port + "/api/v1/account/statistic/"
    package = {"public_key_string": public_key}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)

def wallet_balance(public_key, port):
    url = "http://localhost:" + port + "/api/v1/account/balance/"
    package = {"public_key_string": public_key}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)


if __name__ == "__main__":

    #Tạo 3 wallet tương ứng với 3 node mạng -> trả về 3 ví với public key và private key
    genesis = wallet_create("8050")
    huy = wallet_create("8051")
    tuan = wallet_create("8052")
    
    #Sử dụng response để gọi API
    genesis_wallet = json.loads(genesis)["wallet"]
    huy_wallet = json.loads(huy)["wallet"]
    tuan_wallet = json.loads(tuan)["wallet"]
    time.sleep(10)

    # Mua coin từ hệ thống -> tạo transaction, ở đây delay 10 s để socket xử lý trên tất cả các node và mô phỏng hành động người dùng
    post_transaction(genesis_wallet["private_key"], huy_wallet["public_key"], 500, "EXCHANGE", "8050")
    time.sleep(10)
    post_transaction(genesis_wallet["private_key"], tuan_wallet["public_key"], 300, "EXCHANGE", "8050")
    time.sleep(10)

    # Kiểm tra số dư -> Lúc này, huy gọi API kiểm tra số dư trên node của huy là 8051, tuấn cũng vậy. Huy có 500 và Tuấn có 300
    wallet_balance(huy_wallet["public_key"], "8051")
    wallet_balance(tuan_wallet["public_key"], "8052")

    # Mua stake, lúc này huy giữ nhiều stake nên tỉ lệ tạo block mới sẽ cao nhất
    post_transaction(huy_wallet["private_key"], huy_wallet["public_key"], 400, "STAKE", "8051")
    time.sleep(10)
    post_transaction(tuan_wallet["private_key"], tuan_wallet["public_key"], 200, "STAKE", "8052")
    time.sleep(10)

    # Kiểm tra số dư -> Sau khi mua stake thì mỗi người còn lại 100
    wallet_balance(huy_wallet["public_key"], "8051")
    wallet_balance(tuan_wallet["public_key"], "8052")

    # Chuyển tiền từ Huy -> Tuấn, Huy chuyển cho Tuấn lần lượt 5 và 10 coin
    post_transaction(huy_wallet["private_key"], tuan_wallet["public_key"], 5, "TRANSFER", "8051")
    time.sleep(10)
    post_transaction(huy_wallet["private_key"], tuan_wallet["public_key"], 10, "TRANSFER", "8051")
    time.sleep(10)


    # Kiểm tra số dư -> Huy còn 85 và Tuấn có 115
    wallet_balance(huy_wallet["public_key"], "8051")
    wallet_balance(tuan_wallet["public_key"], "8052")

    # Thống kê tài khoản, lịch sử giao dịch liệt kê tất cả transactions của Huy
    # wallet_statistic(huy_wallet["public_key"], "8051")

   