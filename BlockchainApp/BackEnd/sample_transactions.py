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

    #Mỗi node mạng tạo 1 wallet
    genesis = wallet_create("8050")
    huy = wallet_create("8051")
    tuan = wallet_create("8052")
    
    genesis_wallet = json.loads(genesis)["wallet"]
    huy_wallet = json.loads(huy)["wallet"]
    tuan_wallet = json.loads(tuan)["wallet"]

    # Gán số dư tài khoản bằng 0
    # post_transaction(genesis_wallet["private_key"], genesis_wallet["public_key"], 0, "EXCHANGE", "8050")
    # post_transaction(genesis_wallet["private_key"], huy_wallet["public_key"], 0, "EXCHANGE", "8050")
    # post_transaction(genesis_wallet["private_key"], tuan_wallet["public_key"], 0, "EXCHANGE", "8050")

    #Kiểm tra số dư 
    # wallet_balance(huy_wallet["public_key"], "8051")
    # wallet_balance(tuan_wallet["public_key"], "8052")

    # Mua coin từ hệ thống
    # post_transaction(genesis_wallet["private_key"], huy_wallet["public_key"], 500, "EXCHANGE", "8050")
    # post_transaction(genesis_wallet["private_key"], tuan_wallet["public_key"], 300, "EXCHANGE", "8050")

    #Kiểm tra số dư 
    # wallet_balance(huy_wallet["public_key"], "8050")
    # wallet_balance(tuan_wallet["public_key"], "8050")

    # #Mua stake, lúc này tài khoản 1 giữ nhiều stake nên tỉ lệ tạo block mới sẽ cao nhất
    # post_transaction(huy_wallet["private_key"], huy_wallet["public_key"], 400, "STAKE", "8050")
    post_transaction(tuan_wallet["private_key"], tuan_wallet["public_key"], 200, "STAKE", "8050")

    #Kiểm tra số dư 
    wallet_balance(huy_wallet["public_key"], "8050")
    wallet_balance(tuan_wallet["public_key"], "8050")

    # #Chuyển tiền từ Huy -> Tuấn
    # post_transaction(huy_wallet["private_key"], tuan_wallet["public_key"], 10, "TRANSFER", "8051")
    # post_transaction(huy_wallet["private_key"], tuan_wallet["public_key"], 20, "TRANSFER", "8051")
    # post_transaction(huy_wallet["private_key"], tuan_wallet["public_key"], 30, "TRANSFER", "8051")

    #Kiểm tra số dư 
    # wallet_balance(huy_wallet["public_key"], "8051")
    # wallet_balance(tuan_wallet["public_key"], "8052")

    # #Thống kê tài khoản, liệt kê tất cả transactions
    # wallet_statistic(huy_wallet["public_key"], "8051")


   