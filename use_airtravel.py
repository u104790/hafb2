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


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "| Flight: {1}" \
             "| Seat: {2}" \
             "| Aircraft: {3}" \
             "|".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


def main():
    """
    to test function
    :return:
    """
    flight = make_flight()
    pp(flight.seating)
    pp("Available seats: ", flight.num_available_seats())


if __name__ == '__main__':
    main()
    exit(0)
