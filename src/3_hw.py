# Assignment 3: Simple Temperature Converter
# Instructions:
# Write a program that converts temperatures between Fahrenheit and Celsius.
# The user should be able to input a temperature and specify the unit (C or F),
# and the program will convert it to the other unit.
# Example: "100C" should output "212.0F", and "32F" should output "0.0C"

def temperature_converter(temp_input: str) -> str:
    # TODO: Your code here
    #  Convert the temperature to the other unit
    #  Return the converted temperature
    ...


def test_temperature_converter():
    assert temperature_converter("100C") == "212.0F"
    assert temperature_converter("32F") == "0.0C"
    print("All tests passed!")

# Uncomment to run the test function
# test_temperature_converter()
