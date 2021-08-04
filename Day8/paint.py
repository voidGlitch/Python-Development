
import math
def paint_calc(height,width,cover):
    num_cans = (height * width) / cover
    round_up = math.ceil(num_cans)
    print(f"you'll need {round_up} cans of paints")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)