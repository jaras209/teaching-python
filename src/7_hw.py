# Assignment 7: Dictionary Merging and Analysis
# Instructions:
# Given two dictionaries, merge them and perform the following analysis:
# 1. Count the number of unique keys in the merged dictionary.
# 2. Find the highest value in the merged dictionary.
# The program should return a tuple containing the merged dictionary, the number of unique keys, and the highest value.
# Example input: {'a': 5, 'b': 10}, {'b': 15, 'c': 20}
# Expected output: ({'a': 5, 'b': 15, 'c': 20}, 3, 20)

def merge_and_analyze_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> tuple[dict, int, int]:
    # TODO: Your code here
    #  Merge the dictionaries and perform the analysis
    ...


def test_merge_and_analyze_dicts():
    assert merge_and_analyze_dicts({'a': 5, 'b': 10}, {'b': 15, 'c': 20}) == ({'a': 5, 'b': 15, 'c': 20}, 3, 20)
    assert merge_and_analyze_dicts({'x': 1, 'y': 2}, {'y': 3, 'z': 4}) == ({'x': 1, 'y': 3, 'z': 4}, 3, 4)
    print("All tests passed!")

# Uncomment to run the test function
# test_merge_and_analyze_dicts()
