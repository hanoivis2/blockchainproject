import requests

from blockchain.transaction.wallet import Wallet
from blockchain.utils.helpers import BlockchainUtils


def post_transaction(sender_private_key, receiver_public_key, amount, type):
    url = "http://localhost:8050/api/v1/transaction/create/"
    package = {
        "sender_private_key": sender_private_key,
        "receiver_public_key": receiver_public_key,
        "amount": amount,
        "type": type
    }
    response = requests.post(url, json=package, timeout=15)
    print(response.text)

def wallet_create():
    url = "http://localhost:8052/api/v1/account/create/"
    response = requests.post(url, timeout=15)
    print(response.text)

def wallet_statistic(public_key):
    url = "http://localhost:8050/api/v1/account/statistic/"
    package = {"public_key_string": BlockchainUtils.encode(public_key)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)

def wallet_balance(public_key):
    url = "http://localhost:8050/api/v1/account/balance/"
    package = {"public_key_string": BlockchainUtils.encode(public_key)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)


if __name__ == "__main__":
    # huy = Wallet()
    # vy = Wallet()
    # exchange = Wallet()

    wallet_create()

    # Block size: 2 transactions / block

    # # Forger: Genesis
    # post_transaction(exchange.private_key_string(), exchange.public_key_string(), 400, "EXCHANGE")
    # post_transaction(exchange.private_key_string(), vy.public_key_string(), 200, "EXCHANGE")
    # post_transaction(exchange.private_key_string(), huy.public_key_string(), 10, "EXCHANGE")

    # # Forger: Probably Jane (the Genesis forger has 1 token staked, therefore Jane will most likely be the next forger)
    # post_transaction(huy, vy, 40, "TRANSFER")
    # post_transaction(jane, john, 1, "TRANSFER")

    # # One remaining in transaction pool
    # post_transaction(jane, john, 1, "TRANSFER")

    # post_transaction(huy, huy, 500, "STAKE")
    # post_transaction(vy, vy, 150, "STAKE")

    
    # wallet_balance(exchange)
    # wallet_balance(huy)
    # wallet_create()
    # post_transaction(exchange, exchange, 0, "EXCHANGE")
    # wallet_balance("-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpQ2c9UvIiDOdU4i4yZG0Swyf2\n8ylVMePPSTL0Lqh3Z8gcorYbMLEalUjXPIvuIcdRzjzVUDFt9wWPE4m0InaZH/ul\nUSpEiWpX6zbkrcXsSnVg6v4gHROrYoE0ZkvmuVUAKr/KhXe3S6SN75WQABJG9Ew9\nJhG1hlWvS9TiCqIr6QIDAQAB\n-----END PUBLIC KEY-----\n")
    # wallet_statistic("-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCpQ2c9UvIiDOdU4i4yZG0Swyf2\n8ylVMePPSTL0Lqh3Z8gcorYbMLEalUjXPIvuIcdRzjzVUDFt9wWPE4m0InaZH/ul\nUSpEiWpX6zbkrcXsSnVg6v4gHROrYoE0ZkvmuVUAKr/KhXe3S6SN75WQABJG9Ew9\nJhG1hlWvS9TiCqIr6QIDAQAB\n-----END PUBLIC KEY-----\n")