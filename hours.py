import os


# Clears terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

# Input hours worked, pay rate, and overtime rate
hours = float(input("Hours worked: "))
clear()
reg_rate = float(input("Regular rate:\n"))
clear()
ot_rate = float(input("Overtime rate (if none enter 0):\n"))
clear()
tax_rate = float(input("Tax rate (if none enter 0):\n"))
clear()

# Track inputs
pay = 0
reg_hours = 0
ot_hours = 0

if hours <= 40:
    reg_hours = hours
else:
    reg_hours = 40
    ot_hours = hours % 40	

# Set "pay" to the sum of "reg_hours" times 20 and "ot_hours" times 30
if ot_rate != 0:
	pay = ((reg_hours * reg_rate) + (ot_hours * ot_rate)) * (1 - tax_rate * 0.01)
else:
	pay = (hours * reg_rate) * (1 - tax_rate * 0.01)

# Print pay summary
print(f"Regular hours: {reg_hours}")
print(f"Overtime hours: {ot_hours}")
print(f"Total pay: {pay}")
