"""
List comprehensions
Readable, expressive, and effective
"""
from math import factorial, sqrt


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
    print(info, type(info))
    # Use a list comprehension instead: [ ]
    info2 = [len(str(factorial(x))) for x in range(20)]
    print(info2, type(info2))

    # Set comprehensions: { }
    info3 = {len(str(factorial(x))) for x in range(20)}
    print(info3, type(info3))

    # Dictionary comprehensions: { }
    nba_teams = {'Jazz':'SLC', 'Warriors':'Oakland', 'Lakers':'LA', 'clippers':'LA'}
    print(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    print(teams_nba)

    # Filter predicates
    def is_prime(num):
        """
        Determine if the number is prime
        :param num: input n
        :return: True for prime numbers
                False for non-prime numbers
        """
        if num < 2:
            return False
        for i in range(2, int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    primes = [x for x in range(1001) if is_prime(x)]
    print(len(primes), primes)







if __name__ == '__main__':
    main()
    exit(0)