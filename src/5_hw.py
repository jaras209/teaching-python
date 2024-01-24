# Assignment 5: List Manipulation and Analysis
# Instructions:
# Write a program that takes a list of numbers and performs the following:
# 1. Removes all odd numbers.
# 2. Doubles each even number.
# 3. Returns a tuple containing the modified list and the sum of the original list.
# Example input: [1, 2, 3, 4, 5, 6]
# Expected output: ([4, 8, 12], 21)

def manipulate_list(numbers: list[int]) -> tuple[list[int], int]:
    # TODO: Your code here
    #  Manipulate the list and calculate the sum
    ...


def test_manipulate_list():
    assert manipulate_list([1, 2, 3, 4, 5, 6]) == ([4, 8, 12], 21)
    assert manipulate_list([10, 11, 12, 13, 14]) == ([20, 24, 28], 60)
    print("All tests passed!")

# Uncomment to run the test function
# test_manipulate_list()
