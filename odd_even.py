# odd_even

number = int(input("Which number do you want to check? "))

new_number = number % 2

if new_number == 0:
    print("This is an even number")
else:
    print("This is an odd number")
