"""
Stings and Collections

A sting is an immutable sequence of Unicode code-points
"""

print('This is a string')
print("This is a string too")

# concatenation and Adjacent Strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

# Multi-line Strings and new lines
s3 = """This is 
a multi-line
string"""
print(s3)
s4 = "This is\na multi-line\nstring"
print(s4)
# Support for backslash
s5 = "a\\in a string"
print(s5)
s6 = 'this is "wow"'
print(s6)

# Raw strings
raw_string = r"C:\User\Documents\books"
print(raw_string)

# String as a  sequence
s = "parrot"
print("s[4]", s[4], type(s)) # index notation: 0, 1, 2, etc. You can use help (str) to get all info on strings

print(s, s.capitalize())




