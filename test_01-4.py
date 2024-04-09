# test_01-4.py

import c_wrapper_01_4 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai4", "kadai4.c"])

def test_kadai4():
    # Test with positive number
    assert wrapper.run_kadai4(5) == "その数は 正 です．", "Positive number test failed"
    # Test with negative number
    assert wrapper.run_kadai4(-5) == "その数は 負 です．", "Negative number test failed"
    # Test with zero
    assert wrapper.run_kadai4(0) == "その数は 0 です．", "Zero test failed"

if __name__ == "__main__":
    test_kadai4()
    print("All tests passed!")
