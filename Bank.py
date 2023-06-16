
from datetime import datetime, timedelta

class Bank:
    def __init__(self, name, location, branch) -> None:
        self.name = name
        self.location = location
        self.branch = branch
        self.__balance = 0
        self.accounts = []
        self.transactions = []
        self.canTakeLoan = True
        self.loan = 0
        


    def create_account(self, amount, user):
        user.balance += amount
        self.__balance += amount
        self.accounts.append(user)
    
    def deposit_money(self, amount, user):
        for account in self.accounts:
            if user.nid == account.nid:
                account.balance += amount
                self.__balance += amount
                #time
                now = datetime.now()

                dic = {'name': account.name, 'nid': account.nid, 'info': 'deposited', 'amount': amount, 'time': now + timedelta(hours=5)}
                self.transactions.append(dic)



    def withdraw_money(self, amount, user):
        for account in self.accounts:
            if user.nid == account.nid:
                if amount > account.balance:
                    print("Don't have enough money in your account!")
                elif amount > self.__balance:
                    print("Bank is bankrupted!")
                else:
                    account.balance -= amount
                    self.__balance -= amount
                     #time
                    now = datetime.now()

                    dic = {'name': account.name, 'nid': account.nid, 'info': 'withdrawn', 'amount': amount, 'time': now + timedelta(hours=5)}
                    self.transactions.append(dic)


    
    def check_individual_balance(self, user):
        print(f"------------------> Individual Balance <------------------------")
        for account in self.accounts:
            if user.nid == account.nid:
                print(f"Balance : {account.balance}")

    
    def transfer_money(self, amount, sender, receiver):
        for account in self.accounts:
            #time
            now = datetime.now()
            
            if sender.nid == account.nid:
                if sender.balance >= amount:
                    dic = {'amount': amount, 'info': 'transferred' ,'time': now + timedelta(hours=5), 'nid': sender.nid, 'name': sender.name}
                    self.transactions.append(dic)
                    account.balance -= amount
            if sender.balance >= amount:
                if receiver.nid == account.nid:
                    dic = {'amount': amount, 'info': 'received' ,'time': now + timedelta(hours=5), 'nid': receiver.nid, 'name': receiver.name}
                    self.transactions.append(dic)
                    account.balance += amount
          
    def get_loan_twice_amount(self, user):
        if self.canTakeLoan == True:
            for account in self.accounts:
                if user.nid == account.nid:
                    if self.__balance > account.balance * 2:
                        self.__balance -= account.balance * 2
                        self.loan += account.balance * 2
                    else:
                        print(f"Not have enough money in the bank!!!!!")
        else:
            print("Can not take loan from the bank right now! loan feature is currently off limit.")



    def check_transaction(self, nid):
        print(f"------------------> Transaction history <------------------------")
        for transaction in self.transactions:
            transaction_values = transaction.values()
            if nid in transaction_values:
                if transaction['nid'] == nid:                   
                    print(f"{transaction['name']} {transaction['info']} {transaction['amount']}.00  at {transaction['time']} ")
    
    def check_bank_balance(self, user):
        if user.isAdmin == True:
            return self.__balance
        
    def __loan_feature(self, user, value):
        if user.isAdmin == True:
            self.canTakeLoan = value
          

    def call_private_method(self, user,value):
        self.__loan_feature(user, value)

    def loan_amount(self, user):
        if user.isAdmin == True:
            print(self.loan)
