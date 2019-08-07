"""
Learn about list()
"""


def main():
    """
    Test function
    :return: Nothing
    """
    s = "show how to do it".split()
    print(s, type(s))
    # Access by index
    print("s[3]", s[3])
    print("last member: (s[len(s)-1])", s[len(s)-1]) # very unPythonic
    # Instead use negative index
    print("s[-1]:", s[-1])
    # Uses concept of slicing
    print("From 1st to one before the last member: (s[1:-1])", s[1:-1])
    print("From 1st to skip the first initial only", s[1:])  # the blank in the brackets tells you to to to end
    print("From beg to the 3", s[:3])
    print("from beg to end", s[:])
    # Mad a copy of the list
    t = s
    print("s: ", s)
    print("t: ", t)
    print("t is s: ", t is s)
    t = s[:]  # deep copy
    # or you can use this: t = s.copy()
    # or you can use this: t = list(s)
    print("s: ", s)
    print("t: ", t)
    print("t is s:", t is s)
    print("t == s:", t == s)
    # Shallow copies
    a = [[1, 2], [3, 4]]
    print(a, type(a))
    print("a[a]:", a[0])
    print("a[0][1]:", a[0][1])
    print("a[1][1]:", a[1][1])
    # Copy the list of list
    b = a[:]
    print("b is a:", b is a)
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]:", a[0] is b[0])
    # Let's change on element
    a[0] = [8, 9]
    print("change a[0[ to [8, 9]")
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]:", a[0] is b[0])
    print("a[1] is b[1]:", a[1] is b[1])
    # modify a[1]
    a[1].append(5)
    print("a[1]:", a[1])
    print("b[1]:", b[1])
    print("a[1] is b[1]:", a[1] is b[1])
    print("a:", a)
    print("b:", b)


if __name__ == '__main__':
    main()
    exit(0)