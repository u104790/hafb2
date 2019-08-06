"""
File learn about collections: Tuples, Strings, Range, List, Dictionaries, Sets
"""


def do_tuples():
    """
    practice tuples
    :return: nothing
    """
    # Immutable sequence of arbitrary objects
    # use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size", len(t))
    print("One member: ", t[0])  # by index notation
    # To iterate over a tuple
    for item in t:
        print(item)
    # Single tuples, must end with comma
    t1 = (6,)
    print(t1, type(t1))
    # Another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))


def min_max(items):
    """
    return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def main():
    """
    Test function
    :return: Nothing
    """
    # do_tuples()
    output = min_max([57, 76, 11,12, 90])
    print("min", output[0], type(output[0]))
    print("max", output[1])
    # Tuple unpacking
    lower, upper = min_max([57, 76, 11,12, 90])
    print("min", lower, type(lower))
    print("max", upper)


if __name__ == '__main__':
    main()
    exit(0)