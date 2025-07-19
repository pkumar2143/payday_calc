# Using data from the SQL DB to run calculations.
import sqlite3
import calculator

conn = sqlite3.connect('instance/payday1.db')
cursor = conn.cursor()

# Testing grabbing data & data selection
cursor.execute("SELECT * from expenses")
rows = cursor.fetchall()
for row in rows:
    print(row)
    print(type(row))

print(f"monthly_amt: {rows[0][1]}")

example_balance = 1234.56
for row in rows:
    monthly_charge = row[1]
    example_balance -= monthly_charge
    print(f"Balance after charge {row[0]} in the amount of {monthly_charge:.2f} = {example_balance:.2f}")
# Need a way to involve user's balance, could create another table containing USER and BALANCE

