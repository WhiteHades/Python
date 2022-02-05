row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
mp = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")

h = int(position[0])
v = int(position[1])

# map[h - 1][v - 1] = "X"

row = mp[v - 1]
row[h - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")
