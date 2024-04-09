# test_01-8.py

import c_wrapper_01_8 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai8", "kadai8.c"])

def test_kadai8():
    # Test cases for greeting
    name = "Taro"
    expected_greeting = "こんにちは， Taro さん．"
    assert wrapper.run_kadai8(name).endswith(expected_greeting), f"Expected '{expected_greeting}', got '{wrapper.run_kadai8(name)}'"

    # Additional test case
    name = "Hanako"
    expected_greeting = "こんにちは， Hanako さん．"
    assert wrapper.run_kadai8(name).endswith(expected_greeting), f"Expected '{expected_greeting}', got '{wrapper.run_kadai8(name)}'"

if __name__ == "__main__":
    test_kadai8()
    print("All tests passed!")
