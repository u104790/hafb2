"""
Use flight class
"""
from airtravel import Flight
from airtravel import Aircraft
from pprint import pprint as pp


def main():
    """
    Test function
    :return: Nothing
    """
    f = Flight("SN066")
    print(f, type(f))
    print(f.number())
    # could use: Flight.number(f)
    f2 = Flight("SA013")
    print(f2.number(), f2.airline())
    a1 = Aircraft("G-EUP", "Airbus A31", num_rows=22, num_seats_per_row=6)
    print(a1.registration(), a1.model())
    pp(a1._seating)


if __name__ == '__main__':
    main()
    exit(0)