# test_01-7.py

import c_wrapper_01_7 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai7", "kadai7.c"])

def test_kadai7():
    # Test cases for GCD
    assert wrapper.run_kadai7(60, 48).endswith("gcd is 12"), "GCD of 60 and 48 should be 12"
    assert wrapper.run_kadai7(1071, 462).endswith("gcd is 21"), "GCD of 1071 and 462 should be 21"
    assert wrapper.run_kadai7(0, 5).endswith("gcd is 5"), "GCD of 0 and 5 should be 5"
    assert wrapper.run_kadai7(7, 0).endswith("gcd is 7"), "GCD of 7 and 0 should be 7"

if __name__ == "__main__":
    test_kadai7()
    print("All tests passed!")
