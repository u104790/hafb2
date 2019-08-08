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
    f1 = Flight("SN066",
                Aircraft("G-EUP", "Airbus A319",
                         num_rows=22,
                         num_seats_per_row=6)
                )
    pp(f1._seating)


if __name__ == '__main__':
    main()
    exit(0)