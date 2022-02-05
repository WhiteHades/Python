# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your age? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     if age <= 12:
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# bmi calculator v2

height = input("enter your height in m: ")

weight = input("enter your weight in kg: ")

bmi = round(float(weight) / float(height) ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}. You are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}. You are ebese.")
else:
    print(f"Your BMI is {bmi}. You are clinically obese. Run to the gym NOW!")
