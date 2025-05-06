

def leftover(current_balance=0, expense_list=[0]):
    '''
    Purpose: Compute user's leftover balance after accounting for their upcoming
    and mandatory bills.

    In:
        - current_balance (float): current checking balance.
        - expense_list (list of floats): list of upcoming/mandatory bill amounts.

    Out: current_balance (float): After subtracting all expense values from expense_list
    '''

    dummy_check(expense_value=current_balance, expense_list=expense_list)

    for expense in expense_list:
        dummy_check(expense_value=expense)
        current_balance -= expense

    return current_balance

def mandatory(current_expenses=[0], mandatory_amounts=[0]):
    '''
    Purpose: Determine how much money a user COULD re-allocate.

    In: 
        - current_balances (list): list of each monthly expense total
        - mandatory_amounts (list): list of the portions of each respective 
          monthly expense that is mandatory (e.g. a minimum payment on a credit card.)

    Out: final_non_mandatory_amt (float): amount of money that is non-mandatory/extra.

    '''
    # initial check: make sure each list has matching lengths
    if len(current_expenses) != len(mandatory_amounts):
        raise ValueError("The number of expenses must match the number of mandatory amounts.")
    
    # check: mandatory amounts must be less than or equal to respective expense.
    for i in range(len(mandatory_amounts)):
        if mandatory_amounts[i] > current_expenses[i]:
            raise ValueError("Mandatory amount must be less than or equal to its respective current expense.")
        
    extra_amounts_list = [0]*len(current_expenses)
    for i in range(len(current_expenses)):
        extra_amt = current_expenses[i] - mandatory_amounts[i]
        extra_amounts_list[i] = extra_amt
    
    return float(sum(extra_amounts_list))

def dummy_check(expense_value, expense_list):
    '''
    Purpose: Basic checks for expense values, 
    making sure they exist and are not negative.

    In: expense_value (float), monetary value to check
    Out: Error messages depending on the check.
    '''

    # Expense value in "leftover"
    if expense_value < 0:
        raise ValueError("Expense cannot be negative.")
    
    if expense_value == None or expense_value == '':
        raise ValueError("No balance or expenses listed.")
    
    if ( not isinstance(expense_value, float) ) or ( not isinstance(expense_value, int) ):
        raise TypeError("Expense value must be a float or int.")
    
    # Expense List in "leftover"
    if ( len(expense_list) < 1 ) or ( expense_list == None ):
        raise ValueError("You must enter at least one value")
    
    if ( not isinstance(expense_list, list) ):
        raise TypeError("Expense must be a list.")