# compatibility calculator
print("Welcome to the Compatibility Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

c = combined_string.count('c')
o = combined_string.count('o')
m = combined_string.count('m')
p = combined_string.count('p')
a = combined_string.count('a')
t = combined_string.count('t')
i = combined_string.count('i')
b = combined_string.count('b')
i = combined_string.count('i')
l = combined_string.count('l')
i = combined_string.count('i')
t = combined_string.count('t')
y = combined_string.count('y')

compatibility = c + o + m + p + a + t + i + b + i + l + i + t + y


true_comp = int(str(true) + str(compatibility))

if true_comp < 10 or true_comp > 90:
    print(f"Your score is {true_comp}, you go together like coke and mentos.")
elif true_comp >= 40 and true_comp <= 50:
    print(f"Your score is {true_comp}, you are alright together.")
else:
    print(f"Yourscore is {true_comp}")
