"""
Learn about iterable, iterator objects
Use the built-it in:
  iter(): crate an iterable object,
  next(): fetch the next element in the iterable object
"""
def first(iterable):
    """
    return the next member of the list IF available
    :param iterable: iterable object
    :return: Next member or
    :except: ValueError for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    """
    Test function
    :return: Nothing
    """
    iterable = ["spring", 'summer', 'fall', 'winter']
    iterator = iter(iterable)  # give me an iterator
    print(type(iterator), iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    # print(next(iterator))  # You get an error if you go past your data to be iterated.
    print(first([]))



if __name__ == '__main__':
    main()
    exit(0)
