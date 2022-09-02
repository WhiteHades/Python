mystr = "Table is a good boy"
print(len(mystr))
print(mystr[1:19:2])


print(type(mystr))
# check if all the characters in the text are alphanumeric, meaning alphabet
# and numbers
print(mystr.isalnum())
# Check if all the characters in the text are letters
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is", "are"))
