class Bank_Account:
    def __init__(self, account_holder, pin, initial_balance=0):
        self.pin = pin
        self.account_holder = account_holder
        self.balance = initial_balance
        self.history = []
        self.is_authenticated = False

        user_pin = int(input(f"Enter the pin for {self.account_holder}: "))
        if user_pin == self.pin:
            print("PIN Verified! Access Granted.\n")
            self.is_authenticated = True
        else:
            print("Wrong PIN!")
        

    def deposit(self,): 
        if not self.is_authenticated:
            print("Wrong PIN! Access Denied.")
            return 
        
        amount = int(input("Add Amount you want to add: "))
        self.balance += amount
        self.history.append(f"Deposited: ${amount}")
        print(f"Deposit Success of ${amount}")
    
    def withdraw(self):
        
        if not self.is_authenticated:
            print("Can't Perform Operations, Wrong PIN!")
            return
        
        amount = int(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficiant Funds.")
        else:
            self.balance -= amount
            self.history.append(f"Withdraw: ${amount}")
            print(f"Withdraw Successfull: ${amount}")

    def get_statement(self):
        if not self.is_authenticated:
            print("Cannot View Statements")
            return

        print(f"\n---- Account Statement for {self.account_holder} -----")
        print(f"Current Balance: {self.balance}")
        print("Transection History")
        for item in self.history:
            print(f"- {item}")



my_acc = Bank_Account("Ayan Jamali", pin=2247, initial_balance=500)

my_acc.deposit()
my_acc.withdraw()
my_acc.get_statement()
        
        