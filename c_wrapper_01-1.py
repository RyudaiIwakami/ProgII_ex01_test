# c_wrapper.py

import ctypes
import subprocess

# lib = ctypes.CDLL("./kadai1.so")

def sum_of_two_numbers(a, b):
    process = subprocess.Popen(["./kadai1"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(f"{a}\n{b}\n")
    return output.replace("\n", "").replace(" ", "")