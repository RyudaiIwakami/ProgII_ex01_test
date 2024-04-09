
# c_wrapper_01-3.py

import subprocess

def divide_two_numbers(a, b):
    process = subprocess.Popen(["./kadai3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(f"{a}\n{b}\n")
    result = output.strip().split("\n")[-1]  # Assuming the last line is the result
    return float(result)

