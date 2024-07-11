import requests

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

def wallet_statistic(public_key, port):
    url = "http://localhost:" + port + "/api/v1/account/statistic/"
    package = {"public_key_string": BlockchainUtils.encode(public_key)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)

def wallet_balance(public_key, port):
    url = "http://localhost:" + port + "/api/v1/account/balance/"
    package = {"public_key_string": BlockchainUtils.encode(public_key)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)


if __name__ == "__main__":

    #Mỗi node mạng tạo 1 wallet
    wallet_create("8050")
    wallet_create("8051")
    wallet_create("8052")

    #Gán số dư tài khoản bằng 0
    post_transaction("", "", 0, "EXCHANGE", "8050")
    post_transaction("", "", 0, "EXCHANGE", "8051")
    post_transaction("", "", 0, "EXCHANGE", "8052")

    #Mua coin từ hệ thống
    post_transaction("", "", 500, "EXCHANGE", "8051")
    post_transaction("", "", 300, "EXCHANGE", "8052")

    #Mua stake, lúc này tài khoản 1 giữ nhiều stake nên tỉ lệ tạo block mới sẽ cao nhất
    post_transaction("", "", 400, "STAKE", "8051")
    post_transaction("", "", 200, "STAKE", "8052")

    #Chuyển tiền từ 1 -> 2
    post_transaction("", "", 10, "TRANSFER", "8051")
    post_transaction("", "", 20, "TRANSFER", "8051")
    post_transaction("", "", 30, "TRANSFER", "8051")

    #Kiểm tra số dư 
    wallet_balance("", "8051")
    wallet_balance("", "8052")

    #Thống kê tài khoản, liệt kê tất cả transactions
    wallet_statistic("", "8051")
    wallet_statistic("", "8052")



   