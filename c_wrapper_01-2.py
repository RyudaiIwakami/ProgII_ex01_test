
# c_wrapper_01-2.py

import subprocess

def operate_two_numbers(a, b):
    process = subprocess.Popen(["./kadai2"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(f"{a}\n{b}\n")
    results = output.strip().split("\n")
    return {
        "sum": int(results[0]),
        "difference": int(results[1]),
        "product": int(results[2]),
        "quotient": int(results[3]),
        "remainder": int(results[4])
    }
