"""
Learn about return semantics function arguments in Python
"""
import time


def egg(var):
    """
    returns the variable back to the user
    :param var: input object
    :return: input object
    """
    return var


def sum_two(num1, num2=8):
    """
    Sum two input integer objects
    :param num1: object 1
    :param num2: object 2 (optional) default is = 8
    :return: sum of objects
    """
    total = num1 + num2
    print(num1, " + ", num2, " = ", total)
    return num1 + num2


def banner(message, border='*'):
    """
    Print message in banner form
    :param message: String to print
    :param border: border character for string
    :return:
    """
    print(border*len(message))
    print(message)
    print(border*len(message))


def add_spam(menu=None):
    """
    Add spam to the menu list
    :param menu:
    :return: menu list
    """
    if menu is none:
        menu = []
    menu.append('spam')
    return menu


def main():
    """
    Test function
    :return: Nothing
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)
    n1 = 3
    n2 = 9
    sum_two(n1, n2)
    sum_two(n1)
    banner("Weber State")

    breakfast = ['eggs', 'bacon']
    print("before", breakfast)
    add_spam(breakfast)
    print("after", breakfast)


if __name__ == '__main__':
    main()
    exit(0)