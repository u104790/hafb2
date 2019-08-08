"""
Learn about generator functions
- Describe iterables series with code functions
- Are lazy evaluated: the next value in the sequence is computed on demand
- They can model infinite series/sequences: like data streams, mathematical series with no end
- Can use pipelines

Use the 'yield' keyword
"""


def gen123():
    yield 1
    yield 2
    yield 3


def gen246():
    print('About to yield 2')
    yield 2
    print('About to yield 4')
    yield 4
    print('About to yield 6')
    yield 6
    print('About to return')


def main():
    """
    Test function
    :return: Nothing
    """
    g = gen123()
    print(g, type(g))
    ## yield next value
    # print(next(g))
    # print(next(g))
    # print(next(g))
    # print(next(g))  # causes an error 'StopIteration'
    # iterate over the generator function
    for v in gen123():
        print(v)
    h = gen246()
    print(next(h))
    print(next(h))
    print(next(h))
    print(next(h))


if __name__ == '__main__':
    main()
    exit(0)
