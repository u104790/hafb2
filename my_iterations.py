"""
Wehn working with iterators, generators, etc
Look at the documentation for the itertools module
"""


from itertools import islice, count
from list_comprehensions import is_prime


def main():
    """
    Test function
    :return: Nothing
    """
    # generate the first 1000 primes. List is one time use, must be regenerated to do multiple things
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of first 1K prime numbers: ", list(thousand_primes))
    # Note: If you need to use the object again, you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first 1K prime numbers: ", sum(thousand_primes))
    # Other built-ins use with itertools: any ("or"), all ("and")
    print(any([False, False, True]))  # Like an or
    print(all([False, False, True]))  # Like an and
    # 1361 is the prime number
    print("Are there prime numbers between 1328 and 1361?: ", any(is_prime(x) for x in range(1328, 1362)))



if __name__ == '__main__':
    main()
    exit(0)
