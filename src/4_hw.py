# Assignment 4: Word Frequency Counter
# Instructions:
# Write a program that takes a string and returns a dictionary with each word as a key and its frequency as the value.
# Ignore case (upper/lower case) and punctuation.
# Example input: "Hello world! Hello Python."
# Expected output: {'hello': 2, 'world': 1, 'python': 1}

def word_frequency(text: str) -> dict[str, int]:
    # TODO: Your code here
    #  Process the text and return a dictionary with word frequencies
    ...


def test_word_frequency():
    assert word_frequency("Hello world! Hello Python.") == {'hello': 2, 'world': 1, 'python': 1}
    assert word_frequency("To be, or not to be, that is the question.") == {'to': 2, 'be': 2, 'or': 1, 'not': 1,
                                                                            'that': 1, 'is': 1, 'the': 1, 'question': 1}
    print("All tests passed!")

# Uncomment to run the test function
# test_word_frequency()
