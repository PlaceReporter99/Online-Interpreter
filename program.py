import argparse
from config import language, flag_class
import sys
import subprocess

# Make and import modules from needed_modules
# Take the program file path from -p and the input file path from -i, which will be ommited if input is empty. Take flags from -f as an integer.
# Ensure the flags in the config file are laid out in order, with the first one having a value of 1, the second a value of 2, the third a value of 4, etc.
# If needed you can just call another program.

def evaluate_program(code: str, input: str, flags: flag_class):
    # Insert code for your programming language here, and have it return the output.
    REQUIRE_PRINT = True
    REQUIRE_ERROR = True
    # As a placeholder, we will just output them verbatim
    return str((code, input, flags)), "No error here...", REQUIRE_PRINT, REQUIRE_ERROR


def parse_args():
    parser = argparse.ArgumentParser(
                        prog=language['name'],
                        description=f'An interpreter for {language['name']}.',
                        )

    parser.add_argument('-p', '--program', help="Path to program.")
    parser.add_argument('-i', '--input', help="Path to input.", default="")
    parser.add_argument('-f', '--flag', help="Flags.", default=0, type=int)

    return parser.parse_args()

def get_prog_input_flag():
    data = parse_args()
    with open(data.program) as p:
        code = p.read()
    if data.input == "":
        inp = ""
    else:
        with open(data.input) as i:
            inp = i.read()
    flag = flag_class(data.flag)
    return {
        "code": code,
        "input": inp,
        "flags": flag
    }

if __name__ == "__main__":
    res = evaluate_program(**get_prog_input_flag())
    if res[2]:
        print(res[0])
    if res[3]:
        sys.stderr.write(res[1])
        sys.stderr.flush()