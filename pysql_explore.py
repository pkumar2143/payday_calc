# Using data from the SQL DB to run calculations.
import sqlite3
import calculator

conn = sqlite3.connect('instance/payday.db')
cursor = conn.cursor()

# Test grabbing data & data selection
sql_command = "SELECT * FROM expenses RIGHT JOIN user ON expenses.user_name = user.user_name"

cursor.execute(sql_command)
rows = cursor.fetchall()
for row in rows:
    print(row)
    username0 = row[5]        # NEED TO ENSURE USER FOR THE ENTRIES IS CONSISTENT...
    current_balance = row[7]
    

# # Testing grabbing data & data selection
# cursor.execute("SELECT * from expenses")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#     print(type(row))

# print(f"monthly_amt: {rows[0][1]}")

# example_balance = 1234.56
# for row in rows:
#     monthly_charge = row[1]
#     example_balance -= monthly_charge
#     print(f"Balance after charge {row[0]} in the amount of {monthly_charge:.2f} = {example_balance:.2f}")
# # Need a way to involve user's balance, could create another table containing USER and BALANCE

