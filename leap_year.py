# leap year

year = int(input("Which year do you want to check?\n"))

divisible_by4 = year % 4
divisible_by100 = year % 100
divisible_by400 = year % 400

if divisible_by4 == 0:
    if divisible_by100 != 0:
        print("Leap year.")
    elif divisible_by400 == 0:
        print("Leap year.")
    else:
        print("Not a leap year.")
else:
    print("Not a leap year.")
