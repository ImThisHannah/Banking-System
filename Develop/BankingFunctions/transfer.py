def handle_transfer(checking, savings):
    """
    Handles the transfer of funds between checking and savings accounts.

    Args:
        checking (Account): The checking account object.
        savings (Account): The savings account object.
    """

    print("Which account would you like to transfer from?")
    print("1. Checking")
    print("2. Savings")
    print("3. Cancel")
    account_choice = input("Enter your choice (1-3): ")

    if account_choice == '3':
        return

    try:
        if account_choice in ['1', '2']:
            try:
                amount = float(input("Enter the amount to transfer: "))
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                handle_transfer(checking, savings)
                return 

            if account_choice == '1':
                checking.withdraw(amount)
                savings.deposit(amount)
            else:
                savings.withdraw(amount)
                checking.deposit(amount)

            balances(checking, savings) 

        else:
            raise ValueError("Invalid account choice. Please select 1 for Checking or 2 for Savings.")
    except ValueError as e:
        print(e)
        handle_transfer(checking, savings)

def balances(checking, savings):
    """This function prints the account balances for the user."""
    print("\nHere are your account balances:")
    print(f"Checking: ${checking.get_balance():,.2f}")
    print(f"Savings: ${savings.get_balance():,.2f}")
    