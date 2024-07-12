class AccountModel:
    def __init__(self):
        self.accounts = []
        self.balances = {}
        self.transactions = {}

    def add_account(self, public_key_string):
        if public_key_string not in self.accounts:
            self.accounts.append(public_key_string)
            self.balances[public_key_string] = 0
            self.transactions[public_key_string] = []

    def get_balance(self, public_key_string):
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        return self.balances[public_key_string]
    
    def get_transactions(self, public_key_string):
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        return self.transactions[public_key_string]

    def update_balance(self, public_key_string, amount):
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        self.balances[public_key_string] += amount

    def update_transactions(self, public_key_string, transaction):
        if public_key_string not in self.accounts:
            self.add_account(public_key_string)
        if transaction not in self.transactions[public_key_string]:
            self.transactions[public_key_string].append(transaction)