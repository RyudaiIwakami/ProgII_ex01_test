# c_wrapper_01-4.py

import subprocess

def run_kadai4(input_value):
    process = subprocess.Popen(["./kadai4"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=str(input_value) + "\n")
    return output.strip()
