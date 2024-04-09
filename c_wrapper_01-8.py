# c_wrapper_01-8.py

import subprocess

def run_kadai8(name):
    process = subprocess.Popen(["./kadai8"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate(input=f"{name}\\n")
    return output.strip()
