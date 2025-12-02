import argparse


def main():
    parser = argparse.ArgumentParser(description="AOC - day 1, part 2")
    parser.add_argument("masses_file", help="Path to file with mass values, 1 per line")

    masses_file = parser.parse_args().masses_file
    with open(masses_file, "r") as fh:
        masses = [
            int(mass.strip().rstrip())
            for mass in fh.readlines()
        ]
    fuels = [
        fuel_for_mass(mass)
        for mass in masses
    ]

    print(f"{sum(fuels)}")


def fuel_for_mass(mass):

    base_fuel = (mass // 3) - 2

    if base_fuel > 0:
        return base_fuel + fuel_for_mass(base_fuel)
    else:
        return 0


if __name__ == '__main__':
    main()