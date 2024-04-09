
# test_01-3.py

import c_wrapper_01_3 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai3", "kadai3.c"])

def test_divide_two_numbers():
    # Test for division
    result = wrapper.divide_two_numbers(10, 2)
    assert abs(result - 5.0) < 0.001, f'Expected quotient of 5.0, got {result}'
    
    # Test with floating point result
    result = wrapper.divide_two_numbers(1, 3)
    assert abs(result - 0.333) < 0.001, f'Expected quotient of approximately 0.333, got {result}'

    # Additional test cases as needed
    # Example: Division by zero, negative numbers, etc.

if __name__ == "__main__":
    test_divide_two_numbers()
    print("All tests passed!")
