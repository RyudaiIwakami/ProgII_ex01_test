# test_sum.py

import c_wrapper
import subprocess

output = "それらの和は{}です"

# C言語のコンパイル
subprocess.run(["gcc", "-o", "kadai1", "kadai1.c"])

def test_sum_of_two_numbers():
    # 含むかどうかのテスト
    # print(c_wrapper.sum_of_two_numbers(2, 3))
    # print(output.format(5))
    assert output.format(5) in c_wrapper.sum_of_two_numbers(2, 3)
    assert output.format(0) in c_wrapper.sum_of_two_numbers(-1, 1)
    assert output.format(0) in c_wrapper.sum_of_two_numbers(0, 0)
 
