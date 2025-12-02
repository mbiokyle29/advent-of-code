import argparse
from copy import deepcopy

import numpy


def divide_chunks(array, n=4):
    for i in range(0, len(array), n):  
        yield array[i:i + n] 


def get_val(program, index, n=4):
    return program[index // 4][index % 4]


def set_val(program, index, value, n=4):
    program[index // 4][index % 4] = value


def run_program(program):

    # maybe use operator
    ops = {
        1: lambda l, r: l + r,
        2: lambda l, r: l * r,
    }

    program_length = len(program)
    for i in range(program_length):
        op, left_idx, right_idx, result_idx = program[i]
        if op in [1, 2]:
            left_val = get_val(program, left_idx)
            right_val = get_val(program, right_idx)
            set_val(program, result_idx, ops[op](left_val, right_val))
        elif op == 99:
            return program
        else:
            raise ValueError(f"{op} is not a valid op code")


def main():

    parser = argparse.ArgumentParser(description="AOC - day 2, part 2")
    parser.add_argument("program_file", help="Path to file with int code program")

    program_file = parser.parse_args().program_file
    ops = []
    op_code_length = 4
    with open(program_file, "r") as fh:
        program = list(map(int, fh.read().rstrip().split(",")))

    # chunk op codes and None fill
    program = [
        chunk
        if len(chunk) == op_code_length
        else chunk + [None] * (op_code_length - len(chunk))
        for chunk in divide_chunks(program, op_code_length)
    ]

    for i in range(100):
        for k in range(100):

            program_for_run = deepcopy(program)
            set_val(program_for_run, 1, i)
            set_val(program_for_run, 2, k)
            result_program = run_program(program_for_run)

            if get_val(result_program, 0) == 19690720:
                print(f"i={i}")
                print(f"k={k}")
                print(numpy.matrix(result_program))
                print(f"100 * i + k = {100 * i + k}")

if __name__ == '__main__':
    main()