# Prime number checker

def prime_checker(number):
    prime = True
    for num in range(2, number):
        number % num == 0
        prime = False
    if prime:
        print("This is a prime number")
    else:
        print("This is not a prime number.")


n = int(input("Input number: "))
prime_checker(number=n)
