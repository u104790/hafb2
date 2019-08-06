"""
Learn more about strings
"""


def main():
    """
    Test function
    :return: Nothing
    """
    s1 = "This is super cool"
    print("size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + " " + "State" + " " + "University"
    print(s2)
    # If you need to join large strings, use the join() method
    # instead of + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ": ".join(teams)
    print(record)
    # record = "\n".join(teams)
    # print(record)
    # Split record
    print("split rec", record.split(":"))
    # Partitioning Strings
    # You can use the "dummy" object:_
    departure, _, arrival = "London:Edinburgh".partition(":")
    print(departure, arrival)




if __name__ == '__main__':
    main()
    exit(0)