# How many cans of paint one needs to buy for a given height and width
# Instructions: 1 can of paint can cover 5 square meters

import math


def paint_cal(height, width, cover):
    area = height * width
    numb_of_cans = math.ceil(area / cover)
    print(f"You'll need {numb_of_cans} cans of paint")


test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)
