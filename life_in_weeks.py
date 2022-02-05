# life in weeks (if you live till 90)

age = input("What is your current age?\n")

int_age = 70 - int(age)

days = int_age * 365

weeks = int_age * 52

months = int_age * 12

message = f"You have {days} days, {weeks} weeks and {months} months left if you live till 90"

print(message)
