# c_wrapper_01-7.py

import subprocess

def run_kadai7(x, y):
    process = subprocess.Popen(["./kadai7"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=f"{x}\\n{y}\\n")
    return output.strip()
