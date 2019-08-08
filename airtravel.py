"""
An Flight Class
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """

    def __init__(self, number, aircraft):  # Initializes
        """
        initializes Flight number
        :param number: flight number
        :raise: ValueError(For invalid format)
        """
        # implementation details begin with '_' and tells other that this is private
        # Validate flight number:
        # 5 chars long: AADDD A->ALPHA, D->Digit
        if len(number) != 5:
            raise ValueError("Invalid flight number length {} ".format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("No airline code {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("No route code {}".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):  # Any function that belongs to a class must have self as first parameter
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        return self._number[:2]
    def allocate_seat(self, seat, passenger):
        """
        Allocate a seat to a passenger
        :param seat: A seat designator such as '12c', '21c'
        :param passenger: The passenger name
        :return:
        """
        rows, seat_letter = self._aircraft.seating_plan()
        letter = seat[-1]  # take the letter from the seat
        if letter not in seat_letter:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row{}".format(row_text))

        if row not in rows:
            raise ValueError("Inavalid row number{}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("seat {} already occupied".format(seat))
        self._seating[row][letter] = passenger

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)for row in self._seating if row is not None)

    def make_boarding_class(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self._number(), self._aircraft.model())

    def _passenger_seats(self):
        row_numbers, seat_letter = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letter:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger, "{}{}".format(row, letter))

    @property
    def seating(self):
        return self._seating


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


def main():
    """
    Test function
    :return: Nothing
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)
