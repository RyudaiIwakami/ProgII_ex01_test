# c_wrapper_01-6.py

import subprocess

def run_kadai6():
    process = subprocess.Popen(["./kadai6"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate()
    return output.strip()
