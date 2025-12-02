import argparse
from typing import Literal
from operator import add, sub

Direction = Literal['L', 'R']

class CircularArray:

    def __init__(self, start: int = 50, n: int = 99):
        self._range = n + 1
        self._ptr = start

    def rotate(self, direction: Direction, count: int) -> int:
        op = add if direction == 'R' else sub
        self._ptr = op(self._ptr, count) % self._range
        return self._ptr


def main():
    parser = argparse.ArgumentParser(description="AOC 2025 - day 1, part 1")
    parser.add_argument("rotations_file", help="Path to file with rotation values, 1 per line")

    rotations_file: str = parser.parse_args().rotations_file
    rotations: list[tuple[Direction, int]] = []

    with open(rotations_file, "r") as fh:
        for rec in fh.readlines():
            assert rec[0] == 'L' or rec[0] == 'R'
            direction: Direction = rec[0]
            rotations.append(
                (direction, int(rec[1:]))
            )

    print(f'Loaded {len(rotations)} from {rotations_file}')

    zero_count = 0
    ca = CircularArray(start=50, n=99)
    for (direction, count) in rotations:
        loc = ca.rotate(direction, count)
        if loc == 0:
            zero_count += 1

    print(f'Zero count: {zero_count}')


if __name__ == '__main__':
    main()
