# Using data from the SQL DB to run calculations.
import sqlite3
import calculator

conn = sqlite3.connect('instance/payday.db')
cursor = conn.cursor()

# Test grabbing data & data selection
sql_command = "SELECT * FROM expenses RIGHT JOIN user ON expenses.user_name = user.user_name"

cursor.execute(sql_command)
rows = cursor.fetchall()

# First row will need to have user data.
user_data_row = rows[0]
user_current_balance = user_data_row[7]
print(f"User's current balance = {user_current_balance}, type={type(user_current_balance)}")

# Collect monthly bills amounts
monthly_bills = [0]*len(rows)                  # pre-allotting space
for i in range(len(monthly_bills)):
    monthly_bills[i] = rows[i][1]              # bill amts are index-1 elements of each row
    print(f"Type = {type(monthly_bills[i])}")

print(f"Monthly bills = {type(monthly_bills)}")

monthly_leftover = calculator.leftover(current_balance=user_current_balance, 
                                       expense_list=monthly_bills)

print(f"Amount leftover after all bills paid = {monthly_leftover}")


###########################################
# for row in rows:
#     print(row)
#     username0 = row[5]             # NEED TO ENSURE USER FOR THE ENTRIES IS CONSISTENT...
#     print(f"User = {username0}")
#     current_balance = row[7]
#     print(f"Current balance = {current_balance}")

