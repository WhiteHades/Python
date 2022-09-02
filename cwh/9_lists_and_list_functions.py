grocery = ["harpic", "vim bar", "deodrant", "Bhindi", "lollypop"]
print(grocery[4])


numbers = [2, 7, 9, 11, 2]
numbers.sort()
numbers.reverse()
print(numbers[::3])
print(numbers[1: 5: -1])
print(numbers)

numbers = []
# add numbers at end
numbers.append(90)
numbers.append(2)
numbers.append(3)
# first no. is the index no. (starts from 1), 2nd one is the number
numbers.insert(1, 97)
numbers.remove(2)
# remove last no.
numbers.pop()
print(numbers)

# tuple cannot be changed unlike lists
tp = (1, 3)
print(tp)

a = 1
b = 3
a, b = b, a
print(a, b)
