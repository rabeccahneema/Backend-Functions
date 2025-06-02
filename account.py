
# class Account:
#     def __init__(self, name):
#         self.name = name
#         self.balance = 0.0
#         self.transactions = []
#         self.loan_amount = 0.0
#         self.is_frozen = False
#         self.min_balance = 0.0

    # def deposit(self, amount):
    #     if amount <= 0:
    #         return "Deposit amount must be positive."
    #     self.balance += amount
    #     self.transactions.append(f"Deposited: {amount}")
    #     return f"New balance: {self.balance}"

    # def withdraw(self, amount):
    #     if self.is_frozen:
    #         return "Account is frozen. Cannot withdraw."
    #     if amount <= 0:
    #         return "Withdrawal amount must be positive."
    #     if self.balance - amount < self.min_balance:
    #         return "Insufficient funds to withdraw this amount."
    #     self.balance -= amount
    #     self.transactions.append(f"Withdrew: {amount}")
    #     return f"New balance: {self.balance}"

    # def transfer_funds(self, amount, other_account):
    #     if self.withdraw(amount) == "Insufficient funds to withdraw this amount.":
    #         return "Transfer failed: Insufficient funds."
    #     other_account.deposit(amount)
    #     return f"Transferred {amount} to {other_account.name}. New balance: {self.balance}"

    # def get_balance(self):
    #     return f"Current balance: {self.balance}"

    # def calculate_loan_limit(self):
    #     total_deposits= sum(self.deposits)
    #     return total_deposits//3

    # def request_loan(self, amount):
    #     self.loan_amount += amount
    #     return f"Loan of {amount} approved. Total loan amount: {self.loan_amount}"

    # def repay_loan(self, amount):
    #     if amount > self.loan_amount:
    #         return "Cannot repay more than the loan amount."
    #     self.loan_amount -= amount
    #     return f"Loan repaid: {amount}. Remaining loan amount: {self.loan_amount}"

    # def view_account_details(self):
    #     return f"Account Owner: {self.name}, Current Balance: {self.balance}"

    # def change_account_name(self, new_name):
    #     self.name = new_name
    #     return f"Account owner changed to: {self.name}"

    # def account_statement(self):
    #     statement = "Account Transactions:\n"
    #     for transaction in self.transactions:
    #         statement += transaction + "\n"
    #     return statement.strip()
    #     # print("")

    # def interest_calculation(self):
    #     interest = self.balance * 0.05
    #     self.balance += interest
    #     self.transactions.append(f"Interest applied: {interest}")
    #     return f"New balance after interest: {self.balance}"

    # def freeze_account(self):
    #     self.is_frozen = True
    #     return "Account has been frozen."

    # def unfreeze_account(self):
    #     self.is_frozen = False
    #     return "Account has been unfrozen."

    # def set_minimum_balance(self, amount):
    #     if amount < 0:
    #         return "Minimum balance must be non-negative."
    #     self.min_balance = amount
    #     return f"Minimum balance set to: {self.min_balance}"

    # def close_account(self):
    #     self.balance = 0.0
        # self.transactions.clear()
        # self.loan_amount = 0.0
        # return "Account closed. All balances set to zero."
from datetime import datetime
class Transactions:
    def __init__(self,narration,amount,transaction_type):
        self.amount=amount
        self.narration=narration
        self.transaction_type=transaction_type
        self.date_time=datetime.now()

    def __repr__(self):
        return f"{self.date_time}-{self.transaction_type}:{self.narration} of ${self.amount:.2f}"

class Account:
    def __init__(self,name,account_number):
        self.name=name
        self.account_number=account_number
        self._balance= 0
        self.transaction=[]
        self.minimum_balance=0
        
    def deposit(self,amount):
        if amount<=0:
            return "Deposit amount must be positive"
        self._balance +=amount
        self.transaction.append(Transactions("Deposit",amount,"Credit"))
        return f"confirmed,you have deposited ${amount}.new balance is ${self.get_balance():.2f}"
        
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self._balance - self.minimum_balance:
                return "Insufficient funds for this withdrawal."
        self._balance -= amount
        self.transaction.append(Transactions("Withdrawal", amount, "Debit"))
        return f"Confirmed: You have withdrawn ${amount}. New balance is ${self.get_balance():.2f}"
        
    def  get_balance(self):
        return self._balance
        
    def view_transaction(self):
        return "\n".join(str(transaction) for transaction in self.transaction )
        
    def change_account_owner(self,new_name):
        self.name=new_name
        return  f"Account owner changed to  ${self.name}"
        
    def  set_minimum_balance(self, amount):
        if amount <0:
            return "minimum balance must be positive"
        self.minimum_balance = amount
        return f"minimum balance set to  ${self.minimum_balance:.2f}"
        
    def close_account(self):
        self.balance=0
        self.transaction.clear()
        return "Account closed .All balances and transactions have been reset."

#Each row is an instance of a table