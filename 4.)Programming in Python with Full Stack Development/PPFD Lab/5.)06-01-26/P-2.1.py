class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts = []
    def add_account(self,account):
        self.accounts.append(account)
    def display_accounts(self):
        print(f"Accounts in the bank: {self.bank_name}")
        for acc in self.accounts:
            acc.display_account()
            print('-'*30)
    
    class Account:
        def __init__(self,account_number,customer,balance=0):
            self.account_number = account_number
            self.customer = customer
            self.balance = balance
        def deposit(self,amount):
            if(amount>0):
                self.balance += amount
                print(f"₹Credited amount: ₹{amount}")
                print(f"New Balance after Deposit: ₹{self.balance}")
            else:
                print("Invalid Deposit Amount")
        def withdraw(self,amount):
            if(amount<=self.balance):
                self.balance -= amount
                print(f"₹Debited amount: ₹{amount}")
                print(f"New Balance after Withdrawal: ₹{self.balance}")
            else:
                print("Insufficient Balance")
        def display_account(self):
            print(f"Current Balance: ₹{self.balance},Account Number: {self.account_number}")
            self.customer.display_Customer()
        class Customer:
            def __init__(self, name, customer_id):
                self.name = name
                self.customer_id = customer_id
            def display_Customer(self):
                print(f"Customer Name: {self.name},Customer ID: {self.customer_id}")
cust1=Bank.Account.Customer('Yashwanth',1)
acc1=Bank.Account(12345,cust1,10000)
acc2=Bank.Account(12346,cust1,20000)
bank1=Bank("SBI")
bank2=Bank("Axis")
bank1.add_account(acc1)
bank2.add_account(acc2)
bank1.display_accounts()
bank2.display_accounts()