# c_wrapper_01-5.py

import subprocess

def run_kadai5(input_value):
    process = subprocess.Popen(["./kadai5"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=str(input_value) + "\\n")
    return output.strip()
