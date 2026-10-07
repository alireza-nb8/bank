import random
import json

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.customers = {}
        self.transactions = []

    def signup(self, name, age):
        account_number = str(random.randint(1000, 9999))

        while account_number in self.accounts:
            account_number = str(random.randint(1000, 9999))

        self.accounts[account_number] = 0

        self.customers[account_number] = {
            "name": name,
            "age": age
        }

        return account_number

    def transaction(self, sender, receiver, money):
        if money <=0:
            return False

        if sender == "0000":
            if receiver not in self.accounts:
                return False

            else:
                self.accounts[receiver] += money
                self.transactions.append([sender, receiver, money])
            return True

        if sender not in self.accounts:
            return False

        if receiver not in self.accounts:
            return False

        if self.accounts[sender] < money:
            return False

        self.accounts[sender] -= money
        self.accounts[receiver] += money

        self.transactions.append([sender, receiver, money])
        return True

    def transaction_history(self):
        return self.transactions

    def history(self, account_number):
        result = []

        for transaction in self.transactions:
            if transaction[0] == account_number or transaction[1] == account_number:
                result.append(transaction)

        return result
    
    
# in methode tekrari hast va daghighan kare check ro anjam mideh chon to testa bood neveshtamesh

    def balance_of(self, account_number):
        return self.accounts[account_number]

    def info(self):
        return (self.name, len(self.accounts), len(self.transactions))


    def save(self):
        data = {
            "name": self.name,
                "accounts": self.accounts,
            "customers": self.customers,
            "transactions": self.transactions
        }

        file = open("bank.json", "w")
        json.dump(data, file)
        file.close()

    def load(self, name=None):
        file = open("bank.json", "r")
        data = json.load(file)
        file.close()

        if name is None:
            self.name = data["name"]
        else:
            self.name = name

        self.accounts = data["accounts"]
        self.customers = data["customers"]
        self.transactions = data["transactions"]
