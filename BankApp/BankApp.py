class Bank:
    def __init__(self, Account):
        self.account = Account
        self.__balance = 0
        self.transactionsHistory = []
    
    def checkBalance(self):
        print(f"Available balance: R{self.__balance}")
    
    def showHistory(self):
        if not self.transactionsHistory:
            print("No recorded transactions")
        else:
            for transaction in self.transactionsHistory:
                print(transaction)

            print()

    def deposit(self):
        try:
            
            amount = float(input("Enter the amount you want to deposit: "))

            if amount < 0:
                print("Cannot deposit negative amount!")
            else:
                self.__balance += amount
                self.transactionsHistory.append(f"+R{amount} deposited into acc {self.account}. Available bal R{self.__balance}")
                print(f"+R{amount} deposited into acc {self.account}. New balance R{self.__balance}")
                

        except ValueError:
            print("Invalid Input!")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount you wish to withdraw: "))
            if amount < 0:
                print("Amount cannot be negative...")
            elif amount > self.__balance:
                print("Insufficient funds...")
            else:
                self.__balance -= amount
                self.transactionsHistory.append(f"-R{amount} withdrawn from acc {self.account}. Available bal R{self.__balance}")
                print(f"-R{amount} withdrawn from the acc {self.account}. New balance R{self.__balance}")


        except ValueError:
            print("Invalid Input!")

class Client(Bank):
    def __init__(self, Account, name, email):
        super().__init__(Account)

        self.name = name
        self.email = email
        self.password = None
        self.age = None

    def setPassword(self):
        while True:
            userPassword = input("Enter your password...")
        
            if len(userPassword) < 8:
                print("Password must be 8 characters max. Must Include at least one Uppercase and LowerCase letters.")
            
            elif not any(char.lower() for char in userPassword):
                print("Password must Include at least one lowercase char..")
            
            elif not any(char.isupper() for char in userPassword):
                print("Password must contain uppercase character at least once")

            elif not any(char.isdigit() for char in userPassword):
                print("Password must contain at least one or more digits")
            
            elif not any(char in "$%^@_-&*" for char in userPassword):
                print("Password must contain at least one special character")

            elif " " in userPassword:
                print("Password cannot have empty spaces")
            
            else:
                self.password = userPassword
                print("Password created successfully...")
                break
    
    def setAge(self):

        attempts = 3
        while attempts > 0:
            try:
                userAge = int(input(f"Enter your age: "))

                if userAge == None:
                    print("Field Requied!")
                
                elif userAge < 0:
                    print("Age cannot be negative")
                
                elif userAge < 18:
                    print(f"You are not eligible to create an account. Try again? {attempts - 1} attempts left")

                else:
                    self.age = userAge
                    print("Added age")
                    break
                
            except ValueError:
                print("Invalid Input!")

            attempts -= 1
            if attempts == 0:
                print("Too many failed attempts. Access Blocked")
                exit()

userAccount = Bank("21797975")
userClient = Client("21797975", "Nhlanhla", "nhlanhla1@gmail.com")

is_running = True

while is_running:
    
    print(f"<--Welcome {userClient.name}\n")
    print("1. Login")
    print("2. Check Balance")
    print("3. Make Deposit")
    print("4. Withdraw")
    print("5. Show Transaction History")
    print("6. Exit")


    user = input("Select from the options above: ")

    if user == "1":
        userClient.setPassword()
        userClient.setAge()
        
    elif user == "2":
        userAccount.checkBalance()
        
    elif user == "3":
        userAccount.deposit()      
    
    elif user == "4":
        userAccount.withdraw()
    
    elif user == "5":
        userAccount.showHistory()
        
    elif user == "6":
        print(f"Exiting the program... have a good day {userClient.name}")
        is_running = False
    
    else:
        print("Invalid Choice")