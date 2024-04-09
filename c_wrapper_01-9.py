# c_wrapper_01-9.py

import subprocess

def run_kadai9(x, y):
    process = subprocess.Popen(["./kadai9"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=f"{x}\\n{y}\\n")
    return output.strip()
