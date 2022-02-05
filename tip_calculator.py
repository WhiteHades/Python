# tip calculator

print("Welcome to the tip calculator")

bill = input("What was the total bill? ৳ ")
percentage = input("What percentage tip would you like to give? 2, 3, or 4? ")
split = input("How many people to split the bill? ")

new_bill = float(bill)
new_percentage = float(percentage)
new_percentage2 = (new_percentage / 100) + 1
new_split = float(split)

amount = (new_bill * new_percentage2) / new_split

print(f"Each person should pay: ৳ {round(amount, 2)}")
