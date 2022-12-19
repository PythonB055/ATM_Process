class Atm:
    def __init__(self):

        self.pin=""
        self.balance=0

        self.menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("pin not changed")
            
    def menu(self):
        user_input = input("""
                        Hello, how would you like your proceed ?
                    1. Enter 1 to create pin
                    2. Enter 2 to deposit
                    3. Enter 3 to withdraw
                    4. Enter 4 to Check balance
                    5. Enter 5 to Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")

    def create_pin(self):
        self.pin = input("create your pin")
        print("pin create successfully")
    def deposit(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            amount = int(input("Enter the amout"))
            self.balance = self.balance + amount
            print("Deposit successfully")
        else:
            print("Invalid pin")
    def withdraw(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation successfull")
            else:
                print("Insufficient funds")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter the pin")
        if temp == self.pin:
            print(self.check_balance)
        else:
            print("Invalid pin")
            
