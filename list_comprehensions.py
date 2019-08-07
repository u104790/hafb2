"""
List comprehensions
Readable, expressive, and effective
"""
from math import factorial


def main():
    """
    Test function
    :return: Nothing
    """
    # words = "Today I am very happy to learn aobut list comprehensions".split()
    # print(words)
    # data = []  # empty list
    # for word in words:
    #     # Some analysis
    #     data.append(word)

    # "Filter" data
    # print(data)

    # Task: Find the length of the first 20 factorial numbers
    info = []  # empty list
    for x in range(20):
        # puts factorial into list
        info.append(len(str(factorial(x))))
    # print info
    print(info)
    # Use a list comprehension instead: [ ]
    info2 = [len(str(factorial(x))) for x in range(20)]
    print(info2)




if __name__ == '__main__':
    main()
    exit(0)