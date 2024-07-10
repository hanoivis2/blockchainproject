import requests

from blockchain.transaction.wallet import Wallet
from blockchain.utils.helpers import BlockchainUtils


def post_transaction(sender, receiver, amount, type):
    transaction = sender.create_transaction(receiver.public_key_string(), amount, type)
    url = "http://localhost:8050/api/v1/transaction/create/"
    package = {"transaction": BlockchainUtils.encode(transaction)}
    response = requests.post(url, json=package, timeout=15)
    print(response.text)

def wallet_statistic(account):
    public_key_string = account.public_key_string()
    url = "http://localhost:8050/api/v1/transaction/transactions_statistic/"
    package = {"public_key_string": BlockchainUtils.encode(public_key_string)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)

def wallet_balance(account):
    public_key_string = account.public_key_string()
    url = "http://localhost:8050/api/v1/transaction/balance/"
    package = {"public_key_string": BlockchainUtils.encode(public_key_string)}
    response = requests.get(url, json=package, timeout=15)
    print(response.text)


if __name__ == "__main__":
    john = Wallet()
    jane = Wallet()
    jane.from_key("./keys/staker_private_key.pem")

    exchange = Wallet()

    # Block size: 2 transactions / block

    # Forger: Genesis
    # post_transaction(exchange, jane, 100, "EXCHANGE")
    # post_transaction(exchange, john, 100, "EXCHANGE")
    # post_transaction(exchange, john, 10, "EXCHANGE")
    # post_transaction(jane, jane, 25, "STAKE")

    # Forger: Probably Jane (the Genesis forger has 1 token staked, therefore Jane will most likely be the next forger)
    post_transaction(jane, john, 50, "TRANSFER")

    wallet_statistic(jane)
    wallet_balance(jane)
