"""
Learn how to handle exceptions in Python
"""
import sys

def conver(s):
    """
    Converts a string to integer
    :param s:
    :return:
    """

    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error {}".format(str(e)), file=sys.stderr)
        pass
    return -1


def sqrt(x):
    """
    compute the sqrt using the method of Heron of Alexandria
    :param x: Number to compute the sqrt
    :return: The sqrt of x
    :raise: ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:

        raise ValueError()
    return guess


def main():
    """
    Test function
    :return: Nothing
    """
    # print(conver("11"))
    # print(conver("Hello"))
    # print(conver([1, 4, 8]))
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute the value of negateive numbers")
    print("Done")


if __name__ == '__main__':
    main()
    exit(0)
