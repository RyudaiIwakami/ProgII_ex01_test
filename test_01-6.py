# test_01-6.py

import c_wrapper_01_6 as wrapper
import subprocess

# Compile the C program
subprocess.run(["gcc", "-o", "kadai6", "kadai6.c"])

def test_kadai6():
    expected_lines = [
        "プログラミング演習の第 1 回は 4 月 16 日です",
        "プログラミング演習の第 2 回は 4 月 23 日です",
        "プログラミング演習の第 3 回は 4 月 30 日です",
        "プログラミング演習の第 4 回は 5 月 7 日です",
        "プログラミング演習の第 5 回は 5 月 14 日です",
        "プログラミング演習の第 6 回は 5 月 21 日です",
        "プログラミング演習の第 7 回は 5 月 28 日です",
        "プログラミング演習の第 8 回は 6 月 4 日です",
        "プログラミング演習の第 9 回は 6 月 11 日です",
        "プログラミング演習の第 10 回は 6 月 18 日です",
        "プログラミング演習の第 11 回は 6 月 25 日です",
        "プログラミング演習の第 12 回は 7 月 2 日です",
        "プログラミング演習の第 13 回は 7 月 9 日です",
        "プログラミング演習の第 14 回は 7 月 16 日です",
        "プログラミング演習の第 15 回は 7 月 23 日です",
    ]
    output = wrapper.run_kadai6()
    output_lines = output.split("\\n")
    assert len(output_lines) == len(expected_lines), "Output and expected lines count do not match"
    for i, expected_line in enumerate(expected_lines):
        assert output_lines[i] == expected_line, f"Line {i+1} does not match: {output_lines[i]}"

if __name__ == "__main__":
    test_kadai6()
    print("All tests passed!")
