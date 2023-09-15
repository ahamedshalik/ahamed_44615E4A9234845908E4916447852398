class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        else:
            print("Insufficient funds for withdrawal.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} (Account #{self.__account_number}): ${self.__account_balance}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create a new BankAccount instance
    my_account = BankAccount("12345", "John Doe", 1000)

    # Display initial balance
    my_account.display_balance()

    # Deposit money
    my_account.deposit(500)

    # Withdraw money
    my_account.withdraw(200)

    # Attempt to withdraw more than the balance
    my_account.withdraw(1500)

    # Display final balance
    my_account.display_balance()