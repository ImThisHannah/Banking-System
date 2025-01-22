"""This function handles the transfer process for the user."""
# TODO: Import the Checking from CheckingAccount, Savings from SavingsAccount, and Validation from validation classes
# TODO: These should be imported from the appropriate file in the BankingClasses directory.
from BankingClasses.checking import CheckingAccount
from BankingClasses.savings import SavingsAccount
from BankingClasses.validation import Validation
# TODO: Import the handle_deposit, handle_withdrawal, handle_transfer, and balances functions
# TODO: These should be imported from the appropriate file in the BankingFunctions directory.

from  BankingFunctions.deposit import handle_deposit
from  BankingFunctions.withdraw import handle_withdrawal
from  BankingFunctions.transfer import handle_transfer
from  BankingFunctions.transfer import balances

def main():
    """
    This function is the entry point of the banking system.
    It prompts the user to enter their email and password for authentication.
    If the email and password are valid, the default balances are shown.
    It then presents a menu of options to the user,
    allowing them to make deposits, withdrawals, or transfers between accounts.
    """
    email = input("Enter your email: ")
    print("Your password should be at least 8 characters long,\n"
           "contain at least one uppercase and lowercase letter,\n"
           "one number, and one of the following special characters:!@#$%^&*.")
    password = input("Enter your password: ")

    # TODO: Initialize the attempts variable to 1.
    attempts = 1
    # TODO: Create a while loop to validate the email and password.
    # TODO: The while loop should run as long as the attempts variable is less than 3.
    while attempts < 3:
        # TODO: Validate the email and password using the Validation class.
        if not Validation.validate_email(email) or not Validation.validate_password(password): 
            # If the email and password are invalid,
            # print a message and prompt the user to enter their email and password again.
            print("Invalid email or password. Please try again.")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

        # TODO: Otherwise, break out of the loop.
        else:
            break
    # TODO: If the maximum number of attempts is reached, print a message and exit the program.
        if attempts == 3:
            print("Too many failed login attempts. Exiting.")
            return
    # Set up accounts with default balances.
    checking_account = CheckingAccount(4321.00)
    savings_account = SavingsAccount(6543.21)

    # Print a message for the user inform them of their checking and savings balances
    print("Here are your account balances:")
    # TODO: Use the get_balance method to retrieve the current balance of each account.
    print(f"Checking Account Balance: ${checking_account.get_balance():,.2f}") 
    print(f"Savings Account Balance: ${savings_account.get_balance():,.2f}") 
    # TODO: Write while loop to present options for the user.
    # TODO: Present a menu of options to the user.
    # TODO: Allowing them to make deposits, withdrawals, or transfers between accounts.
    while True:
        print("\nSelect an option:")
        print("1. Deposit to Checking")
        print("2. Withdraw from Checking")
        print("3. Deposit to Savings")
        print("4. Withdraw from Savings")
        print("5. Transfer from Checking to Savings")
        print("6. Transfer from Savings to Checking")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        # TODO: Create a list of valid choices.
        valid_choices = ['1', '2', '3', '4', '5', '6', '7']
            # TODO: Use if/elif conditional statements to check the user's choice.
            # TODO: If the choice is in the list of valid choices, call the appropriate function.
            # TODO: Pass in the checking_account and savings_account objects.
        if choice in valid_choices:
            if choice == '1':
                handle_deposit(checking_account)
        elif choice == '2':
            handle_withdrawal(checking_account)
        elif choice == '3':
            handle_deposit(savings_account)
        elif choice == '4':
            handle_withdrawal(savings_account)
        elif choice == '5':
            handle_transfer(checking_account, savings_account) 
        elif choice == '6':
            handle_transfer(savings_account, checking_account)
        elif choice == '7':
            print("Exiting...")
            break

        # TODO: If the user enters an invalid choice, print a message.
        else:
            print("Invalid choice. Please select a number between 1 and 7.")
if __name__ == "__main__":
    main()
