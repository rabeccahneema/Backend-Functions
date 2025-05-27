
class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0
        self.transactions = []
        self.loan_amount = 0.0
        self.is_frozen = False
        self.min_balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        return f"New balance: {self.balance}"

    def withdraw(self, amount):
        if self.is_frozen:
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if self.balance - amount < self.min_balance:
            return "Insufficient funds to withdraw this amount."
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        return f"New balance: {self.balance}"

    def transfer_funds(self, amount, other_account):
        if self.withdraw(amount) == "Insufficient funds to withdraw this amount.":
            return "Transfer failed: Insufficient funds."
        other_account.deposit(amount)
        return f"Transferred {amount} to {other_account.owner}. New balance: {self.balance}"

    def get_balance(self):
        return f"Current balance: {self.balance}"

    def request_loan(self, amount):
        self.loan_amount += amount
        return f"Loan of {amount} approved. Total loan amount: {self.loan_amount}"

    def repay_loan(self, amount):
        if amount > self.loan_amount:
            return "Cannot repay more than the loan amount."
        self.loan_amount -= amount
        return f"Loan repaid: {amount}. Remaining loan amount: {self.loan_amount}"

    def view_account_details(self):
        return f"Account Owner: {self.owner}, Current Balance: {self.balance}"

    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner changed to: {self.owner}"

    def account_statement(self):
        statement = "Account Transactions:\n"
        for transaction in self.transactions:
            statement += transaction + "\n"
        return statement.strip()

    def interest_calculation(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest applied: {interest}")
        return f"New balance after interest: {self.balance}"

    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance must be non-negative."
        self.min_balance = amount
        return f"Minimum balance set to: {self.min_balance}"

    def close_account(self):
        self.balance = 0.0
        self.transactions.clear()
        self.loan_amount = 0.0
        return "Account closed. All balances set to zero."