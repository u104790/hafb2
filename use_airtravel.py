"""
Use flight class
"""
from airtravel import Flight
from airtravel import Aircraft
from pprint import pprint as pp


def make_flight():
    """
    Test function
    :return: Nothing
    """
    flight = Flight("SN066",
                Aircraft("G-EUP", "Airbus A319",
                         num_rows=22,
                         num_seats_per_row=6)
                )
    # pp(f1._seating)
    flight.allocate_seat("02A", "Guido Van Rossum")
    flight.allocate_seat("12B", "Rasums Lerdorf")
    flight.allocate_seat("15F", "Bjare Stroustrup")
    flight.allocate_seat("03A", "Larry Wall")
    flight.allocate_seat("16F", "Yukihiro Matsumoto")
    return flight


def main():
    f1 = make_flight()
    pp(f1._seating)
    pp("Available seats: ", f1.num_available_seats())



if __name__ == '__main__':
    main()
    exit(0)