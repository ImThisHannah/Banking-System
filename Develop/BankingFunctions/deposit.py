def handle_deposit(checking, savings):
    """
    This function handles the deposit process for the user.

    Parameters:
    checking (Account): The checking account object.
    savings (Account): The savings account object.
    """
    print("Which account would you like to make a deposit into?")
    print("1. Checking Account")
    print("2. Savings Account")
    print("3. Quit")
    
    account_choice = input("Enter the number of your choice: ")

    if account_choice == '3':
        print("Exiting deposit process.")
        return
    
    try:
        # Validate if the user entered a valid choice
        if account_choice not in ['1', '2']:
            raise ValueError("Invalid choice. Please enter 1 for Checking, 2 for Savings, or 3 to Quit.")
        
        # Prompt for the deposit amount
        deposit_amount = input("Enter the amount to deposit: ")
        
        try:
            deposit_amount = float(deposit_amount)
            
            if deposit_amount <= 0:
                raise ValueError("Deposit amount must be greater than zero.")
        except ValueError:
            print("Invalid amount entered. Please enter a valid numeric value.")
            handle_deposit(checking, savings)
            return
        
        # Handle deposit based on the user's account choice
        if account_choice == '1':
            checking.deposit(deposit_amount)
            print(f"Deposit successful! Your new Checking Account balance is: ${checking.balance:,.2f}")
        elif account_choice == '2':
            savings.deposit(deposit_amount)
            print(f"Deposit successful! Your new Savings Account balance is: ${savings.balance:,.2f}")

    except ValueError as e:
        print(e)
        handle_deposit(checking, savings)
