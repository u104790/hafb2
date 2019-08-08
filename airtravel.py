"""
An Flight Class
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """

    def __init__(self, number):  # Initializes
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

    def number(self):  # Any function that belongs to a class must have self as first parameter
        """
        Flight Number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        return self._number[:2]


class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

        rows, seats = self.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]

    @property
    def seating(self):
        return self._seating


def main():
    """
    Test function
    :return: Nothing
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)
