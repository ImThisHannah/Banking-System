"""This function handles the deposit process for the user."""
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation
from BankingFunctions import handle_deposit, handle_withdrawal, handle_transfer, balances 

# TODO: Build out the handle_deposit function
# TODO: Pass in the checking account and savings account objects.
def handle_deposit():
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit?")
    # TODO: Prompt the user to select an account and make a deposit.
    # TODO: If the user chooses to quit, return from the function.
    print("1. Checking")
    print("2. Savings")
    print("3. Cancel")
    account_choice = input("Enter your choice (1-3): ")
    if account_choice == '3':
        return

    try:
        # TODO: If the selection is in a list of valid choices, i.e ['1', '2']
        if account_choice in ['1', '2']:
            try:
                # TODO: Prompt the user to enter the amount to deposit and convert it to a float.
                amount = float(input("Enter the amount to deposit: "))
            # Use the ValueError as an exception.
            except ValueError:
                # TODO: Print an error message if the user enters an invalid amount.
                print("Invalid amount. Please enter a numeric value.")
                # TODO: Call the handle_deposit function recursively for an invalid amount.
                handle_deposit(checking, savings)
                # TODO: Ensure the function returns after the recursive call.
                return 
            # TODO: Add an if/else conditional statement to check the account choice,
            if:
                # TODO: Call the withdraw method on the appropriate account.
                checking.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Deposited ${amount:,.2f} to your Checking Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Savings Account Balance: ${savings.get_balance():,.2f}")
            else:
                # TODO: Call the deposit methods on the appropriate account.
                savings.deposit(amount)
                # TODO: Add a print statement to display the updated balance after the deposit
                print(f"Deposited ${amount:,.2f} to your Savings Account.")
                # TODO: Format the balance to two decimal places and thousands.
                print(f"New Savings Account Balance: ${savings.get_balance():,.2f}")
        else:
            # TODO: Raise a ValueError with a message stating the user entered an invalid choice.
            raise ValueError("Invalid account choice. Please select 1 for Checking or 2 for Savings.")
    # If the user enters an invalid choice,
    # Print the ValueError message and call the handle_deposit function recursively.
    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
