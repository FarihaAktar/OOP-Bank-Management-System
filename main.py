from Bank import Bank
from Users import User, Admin




bank = Bank("Fariha-Bank", "Mirpur", "Dhaka")


#create account
snigdha = User("Snigdha", "Puran Dhaka", "01232434", "111")
bank.create_account(5000, snigdha)
sonia = User("Sonia", "Narayonganj", "0125234", "112")
bank.create_account(100000, sonia)

#create admin
fariha = Admin("Fariha", "Manikdi", "3636663", "222")

bank.create_account(10, fariha)

#deposit money
bank.deposit_money(1000, snigdha)
bank.deposit_money(20000, snigdha)


#withdraw money
bank.withdraw_money(5000, snigdha)

#check individual balance
bank.check_individual_balance(snigdha)

#transfer money to another account
bank.transfer_money(20000, sonia, snigdha)

# transaction history
bank.check_transaction('111')
bank.check_transaction('112')

#check individual balance
bank.check_individual_balance(snigdha)

#--------------Admin-------------
# check bank balance
print(f"Total Balance : {bank.check_bank_balance(fariha)}")

# on or off the loan feature of the bank.
bank.call_private_method(fariha, False)

bank.get_loan_twice_amount(sonia)

bank.loan_amount(fariha)


bank.call_private_method(fariha, True)
bank.get_loan_twice_amount(snigdha)
bank.loan_amount(fariha)

# check bank balance
print(f"Total Balance : {bank.check_bank_balance(fariha)}")



