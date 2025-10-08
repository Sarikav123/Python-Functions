#Create a function calculate_area(length, width=5) that calculates the area of a rectangle.
#If only the length is provided, the function should assume the width is 5. Show how the function behaves when called with and without the width argument.


def cal_area(lng, width=5):
    area = lng * width
    print(f' area of rectangle is {area}')

cal_area(7)
cal_area(9,6)
