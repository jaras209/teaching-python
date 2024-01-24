# Assignment 2: Basic Arithmetic Quiz
# Instructions:
# Create a simple quiz that asks the user to solve 3 different arithmetic problems.
# The program should ask a question, take the user's answer, and then give them a score at the end.
# Example: For questions 3 + 4, 5 * 6, and 9 - 2, correct answers would be 7, 30, and 7.

def arithmetic_quiz() -> int:
    # TODO: Your code here
    #  Ask three arithmetic questions
    #  Keep track of the number of correct answers
    #  Return the user's score
    ...


def test_arithmetic_quiz():
    # You can modify test inputs and expected outputs here
    expected_score = 3  # Assuming all answers are correct
    actual_score = arithmetic_quiz()
    assert actual_score == expected_score, f"Expected score: {expected_score}, but got: {actual_score}"
    print("Quiz passed!")

# Uncomment to run the test function
# test_arithmetic_quiz()
