class Bank:
    def __init__(self):
        self.accounts = {}
    def add_Account(self, account_number, account):
        self.accounts[account_number] = account
    def remove_Account(self, account_number):
        del self.accounts[account_number]
    def get_Account(self, account_number):
        return self.accounts[account_number]
    def display_Account(self):
        for account_number, account in self.accounts.items():
            print(account_number, account)
    
    class Account:
        def __init__(self, customer_name, customer_age, customer_address):
            self.customer_name = customer_name
            self.customer_age = customer_age
            self.customer_address = customer_address
        def display_Customer_details(self):
            print(self.customer_name, self.customer_age, self.customer_address)
    
        class Customer:
            def deposit(self):
                self.balance += amount
            def withdraw(self):
                self.balance -= amount
            def display_Balance(self):
                print(self.balance)

