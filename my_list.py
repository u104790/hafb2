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
    print("change a[0] to [8, 9]")
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
    # Repetition
    c = [21, 37]
    d = c * 4
    print("c:", c)
    print("d:", d)
    # All point ot the same object
    s = [[-1, 1]]*5
    print(s)
    s[1].append(7)
    print(s)
    # index() method for lists
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    i = w.index('fox')
    print("the index of 'fox' entry is:", i, w[i])
    # If no index is found, it will throw a ValueError
    # i = w.index('cat')  # cat is not in list so we get an error
    # print("The index of 'cat' entry is:", i, w[i])

    # Membership testing with: count()
    print("'the' value is: ", w.count("the"))
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])
    # Removing elements form list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(len(w), w)
    del w[3]  # delete using index
    print(len(w), w)
    # remove using: remove()
    w.remove("over")
    print(len(w), w)
    # same as
    del w[w.index('dog')]
    print(len(w), w)
    # Rearranging list of elements
    g = [1, 11, 21, 1211, 112111]
    print("g:", g)
    g.reverse()  # This is a permanent change in order
    print("reverse g:", g)
    g.reverse()  # This is a permanent change in order
    print("reverse g:", g)

    # Sort method accepts two argument, key and reverse
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print("d:      ", d)
    d.sort()
    print("Sort d: ", d)
    d.sort(reverse=True)
    print("Sort.reverse d: ", d)
    # sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print("w:      ", w)
    w.sort()
    print("Sort w: ", w)
    print("Sort.reverse w: ", w)
    w.sort(key=len)
    print(w)







if __name__ == '__main__':
    main()
    exit(0)