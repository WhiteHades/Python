# dictionary = key value pairs

di = {"Harry": "burger", "Aj": "Rice", "Ai": {
    "B": "maggie", "L": "ruti", "D": "Chicken"}}
print(di["Ai"]["B"])

di["Ankit"] = "Junk food"
di["Aurangzeb"] = "kabab"
del di["Aurangzeb"]
print(di)


di = {"Harry": "burger", "Aj": "Rice", "Ai": {
    "B": "maggie", "L": "ruti", "D": "Chicken"}}

dl = di.copy()  # doesn't touch di, changes the copy of di
del dl["Harry"]
print(di)
