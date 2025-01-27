def handle_withdrawal(checking, savings):
    """
    Handles the withdrawal of funds for checking and savings accounts.

    Parameters:
    - checking (CheckingAccount): The checking account object.
    - savings (SavingsAccount): The savings account object.
    """
    print("Which account would you like to make a withdrawal from?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("3. Quit")
    
    account_choice = input("Enter the number of your choice: ")

    if account_choice == '3':
        print("Exiting withdrawal process.")
        return
    
    try:
        # Validate if the user entered a valid choice
        if account_choice not in ['1', '2']:
            raise ValueError("Invalid choice. Please enter 1 for Checking, 2 for Savings, or 3 to Quit.")
        
        # Prompt for the withdrawal amount
        withdrawal_amount = input("Enter the amount to withdraw: ")
        
        try:
            withdrawal_amount = float(withdrawal_amount)
            
            if withdrawal_amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
        except ValueError:
            print("Invalid amount entered. Please enter a valid numeric value.")
            handle_withdrawal(checking, savings)
            return
        
        # Handle withdrawal based on the user's account choice
        if account_choice == '1':
            if checking.balance < withdrawal_amount:
                print("Insufficient funds in Checking Account.")
            else:
                checking.withdraw(withdrawal_amount)
                print(f"Withdrawal successful! Your new Checking Account balance is: ${checking.balance:,.2f}")
        elif account_choice == '2':
            if savings.balance < withdrawal_amount:
                print("Insufficient funds in Savings Account.")
            else:
                savings.withdraw(withdrawal_amount)
                print(f"Withdrawal successful! Your new Savings Account balance is: ${savings.balance:,.2f}")

    except ValueError as e:
        print(e)
        handle_withdrawal(checking, savings)
