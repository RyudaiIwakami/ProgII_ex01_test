
# test_01-2.py

import c_wrapper_01_2 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai2", "kadai2.c"])

def test_operate_two_numbers():
    # Test for sum, difference, product, quotient, and remainder
    result = wrapper.operate_two_numbers(10, 5)
    assert result["sum"] == 15, f'Expected sum of 15, got {result["sum"]}'
    assert result["difference"] == 5, f'Expected difference of 5, got {result["difference"]}'
    assert result["product"] == 50, f'Expected product of 50, got {result["product"]}'
    assert result["quotient"] == 2, f'Expected quotient of 2, got {result["quotient"]}'
    assert result["remainder"] == 0, f'Expected remainder of 0, got {result["remainder"]}'

    result2 = wrapper.operate_two_numbers(10, 3)
    assert result2["sum"] == 13, f'Expected sum of 13, got {result2["sum"]}'
    assert result2["difference"] == 7, f'Expected difference of 7, got {result2["difference"]}'
    assert result2["product"] == 30, f'Expected product of 30, got {result2["product"]}'
    assert result2["quotient"] == 3, f'Expected quotient of 3, got {result2["quotient"]}'
    assert result2["remainder"] == 1, f'Expected remainder of 1, got {result2["remainder"]}'
    
    # Additional test cases as needed
    # Example: Negative numbers, zero, etc.

if __name__ == "__main__":
    test_operate_two_numbers()
    print("All tests passed!")
