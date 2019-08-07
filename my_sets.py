"""
Learn about sets
An unordered collection of unique, immutable objects
Define it using { } but you don't need a key.
"""



def main():
    """
    Test function
    :return: Nothing
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 1]
    print("Print of data:            ", data, type(data))
    # eliminate duplicates
    sdata = set(data)
    print("Data is turned into a set:", sdata, type(sdata), "duplicates are removed")
    # Iterate with for
    for item in sdata:
        print(item)
    # Supports membership testing: in, not in
    print("Asks if 5 is in data set:", 5 in sdata)
    # Adding elements to sets: we use add (just one object) and update (a bunch of objects)
    sdata.add(45)
    print("added 45 to set", sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])
    print("a bunch of numbers, but will only import unique numbers:", sdata)
    # removing elements
    # can cause an error if number is not in set
    sdata.remove(44)
    print("removes 44:", sdata)
    # sdata.remove(77)
    # print("remove 77, but 77 not in set:", sdata)
    # discard() method: does not raise any error
    sdata.discard(77)
    print(sdata)
    # Copying sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)
    ######## Define some sets
    blue_eyes = {'olivia', 'harry', 'lily', 'jack'}
    blond_hair = {'harry', 'jack', 'amelia', 'mia', 'joshua',}
    smell_hcn = {'harry', 'amelia'}
    tast_ptc = {'harry', 'lily', 'amelia', 'lola'}
    o_blood = {'mia', 'joshua', 'lily', 'olivia'}
    b_blood = {'amelia', 'jack'}
    a_blood = {'harry'}
    ab_blood = {'joshua', 'lola'}
    print(blue_eyes.union(blond_hair))
    print(blue_eyes.intersection(tast_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(tast_ptc.issuperset((smell_hcn)))






if __name__ == '__main__':
    main()
    exit(0)