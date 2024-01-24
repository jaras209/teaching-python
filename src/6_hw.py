# Assignment 6: String Reversal and Palindrome Checker
# Instructions:
# Write a program that reverses a string and checks if it is a palindrome.
# A palindrome is a word that reads the same backward as forward.
# The program should return a tuple containing the reversed string and a boolean indicating if it's a palindrome.
# Example input: "racecar"
# Expected output: ("racecar", True)

def reverse_and_check_palindrome(text: str) -> tuple[str, bool]:
    # TODO:Your code here
    #  Reverse the string and check if it is a palindrome
    ...


def test_reverse_and_check_palindrome():
    assert reverse_and_check_palindrome("racecar") == ("racecar", True)
    assert reverse_and_check_palindrome("level") == ("level", True)
    assert reverse_and_check_palindrome("madam") == ("madam", True)
    assert reverse_and_check_palindrome("python") == ("nohtyp", False)
    print("All tests passed!")

# Uncomment to run the test function
# test_reverse_and_check_palindrome()
