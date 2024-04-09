# test_01-5.py

import c_wrapper_01_5 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai5", "kadai5.c"])

def test_kadai5():
    # Test cases for each season
    assert wrapper.run_kadai5(3).endswith("春です．"), "March should be spring"
    assert wrapper.run_kadai5(7).endswith("夏です．"), "July should be summer"
    assert wrapper.run_kadai5(10).endswith("秋です．"), "October should be autumn"
    assert wrapper.run_kadai5(1).endswith("冬です．"), "January should be winter"
    # Test case for invalid month
    assert wrapper.run_kadai5(13).endswith("月はありません．"), "13 is an invalid month"

if __name__ == "__main__":
    test_kadai5()
    print("All tests passed!")
