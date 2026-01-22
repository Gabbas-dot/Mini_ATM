class ATM:
    """
    Handles core ATM operations such as
    checking balance, depositing, and withdrawing money.
    """

    def __init__(self):
        self.balance = 0  # balance stored as integer amount

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount


class ATMController:
    """
    Manages user interaction and connects input/output
    with ATM business logic.
    """

    def __init__(self):
        self.atm = ATM()

    def get_amount(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def display_menu(self):
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def check_balance(self):
        balance = self.atm.get_balance()
        print(f"Your current balance is: ${balance}")

    def deposit_money(self):
        try:
            amount = self.get_amount("Enter deposit amount: ")
            self.atm.deposit(amount)
            print("Deposit successful.")
        except ValueError as error:
            print(error)

    def withdraw_money(self):
        try:
            amount = self.get_amount("Enter withdrawal amount: ")
            self.atm.withdraw(amount)
            print("Withdrawal successful.")
        except ValueError as error:
            print(error)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit_money()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


def main():
    controller = ATMController()
    controller.run()


if __name__ == "__main__":
    main()
