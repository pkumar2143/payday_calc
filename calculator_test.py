from calculator import *

# All good
try:
    current_balance = 1000
    expense_list = [101, 204.56, 43.5]
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except:
    print("This test went wrong\n")

# Negative current_balance
try:
    current_balance = -1
    expense_list = [101, 204.56, 43.5]
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except:
    print("The current balance is negative.\n")

# Negative expenses
try:
    current_balance = -1
    expense_list = [101, 204.56, -43.5]
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except:
    print("At least one expense is negative.\n")

# Empty balance
try:
    current_balance = None
    expense_list = [101, 204.56, -43.5]
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except:
    print("Current balance does not exist.\n")

# None entry for expense_list
try:
    current_balance = 1002
    expense_list = None
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except ValueError as e:
    print(f"Error: Some value does not make sense. Details: {e}")
except TypeError as e:
    print(f"Error: Some entries not of the right type. Details: {e}")

# Type error for expense_list
try:
    current_balance = 1002
    expense_list = ""
    print(f"Current balance = {current_balance}")
    print(f"Expense List = {expense_list}")
    print(leftover(current_balance=current_balance, expense_list=expense_list),"\n")
except ValueError as e:
    print(f"Error: Some value does not make sense. Details: {e}")
except TypeError as e:
    print(f"Error: Some entries not of the right type. Details: {e}")


print("hello")

