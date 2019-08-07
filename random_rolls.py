"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics


def roll_die(num):
    """
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    Index 1 maps to 2
    """
    freq = [0] * 6  # initial value to zero
    for roll in range(num):
        n = random.randrange(1, 7)
        freq[n-1] += 1
        # print(random.randint(1, 6))
    return freq

def main():
    """
    Test function
    :return: Nothing
    """
    num = int(input("How many times do you need to roll"))
    l = roll_die(num)
    for roll, total in enumerate(l):
        print("Total rolls of {} = {}".format(roll+1, total))

    print("Mean = {}".format(statistics.mean(l)))
    print("Median = {}".format(statistics.median(l)))


if __name__ == '__main__':
    main()
    exit(0)