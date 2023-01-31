"""Implement a Python function that takes a list of integers and a target number as input, and returns a tuple of two integers that add up to the target number."""

target = int(input("Enter Target: "))
def func(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] < target:
                return (numbers[i]), numbers[j]

numbers = [2, 5, 7, 33, 24, 755, 24, 26, 13, 62, 11, 22, 44, 66, 36]

print(func(numbers, target))