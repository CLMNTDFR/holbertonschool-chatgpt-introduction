#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class for managing a balance through deposits and withdrawals.
    """

    def __init__(self):
        """
        Initializes a new checkbook instance with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the balance.

        Parameters:
        amount (float): The amount to be deposited.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Subtracts a specified amount from the balance if funds are sufficient.

        Parameters:
        amount (float): The amount to be withdrawn.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to run the checkbook manager.
    """
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
