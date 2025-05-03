

def leftover(current_balance=0, expense_list=[0]):
    '''
    Purpose: Compute user's leftover balance after accounting for their upcoming
    and mandatory bills.

    In:
        - current_balance (float): current checking balance.
        - expense_list (list of floats): list of upcoming/mandatory bill amounts.

    Out:
        - current_balance (float): After subtracting all expense values from expense_list
    '''
    
    if ( len(expense_list) < 1 ) or ( expense_list == None ):
        raise ValueError("You must enter at least one value")
    
    if ( not isinstance(expense_list, list) ):
        raise TypeError("Expense must be a list.")

    dummy_check(current_balance)

    for expense in expense_list:
        dummy_check(expense_value=expense)
        current_balance -= expense

    return current_balance

def dummy_check(expense_value):
    '''
    Purpose: Basic checks for expense values, 
    making sure they exist and are not negative.

    In: expense_value (float), monetary value to check
    Out: Error messages depending on the check.
    '''

    if expense_value < 0:
        raise ValueError("Expense cannot be negative.")
    
    if expense_value == None or expense_value == '':
        raise ValueError("No balance or expenses listed.")
    
    if ( not isinstance(expense_value, float) ) or ( not isinstance(expense_value, int) ):
        raise TypeError("Expense value must be a float or int.")