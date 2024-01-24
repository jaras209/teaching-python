# Assignment 1: Personalized Greeting Card Generator
# Instructions:
# Write a Python program that asks the user for their name and their favorite color.
# Then, print a personalized greeting message and a statement about their favorite color.
# Example output for inputs "Alice" and "Blue": "Hello, Alice! I see your favorite color is Blue."

def generate_greeting(name: str, color: str):
    # TODO: Your code here
    ...


def test_generate_greeting():
    assert generate_greeting("Alice", "Blue") == "Hello, Alice! I see your favorite color is Blue."
    assert generate_greeting("Bob", "Green") == "Hello, Bob! I see your favorite color is Green."
    print("All tests passed!")

# Uncomment to run the test function
# test_generate_greeting()
