# Write a Python function find_maximum(numbers) that takes a list of integers and
# returns the maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.


def findmax(number):
    max_num = number[0]
    for num in number:
        if num>max_num:
            max_num = num
    return max_num

list1 = [7,5,45,76,89,4,3]
print(findmax(list1))

