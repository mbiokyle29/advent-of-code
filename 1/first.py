import argparse


def main():
    parser = argparse.ArgumentParser(description="AOC - day 1, part 1")
    parser.add_argument("masses_file", help="Path to file with mass values, 1 per line")

    masses_file = parser.parse_args().masses_file
    with open(masses_file, "r") as fh:
        masses = [
            int(mass.strip().rstrip())
            for mass in fh.readlines()
        ]
    fuels = [
        (mass // 3) - 2
        for mass in masses
    ]

    print(f"{sum(fuels)}")

if __name__ == '__main__':
    main()