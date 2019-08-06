"""
Learn about Control Flow in Python
"""

# IF Statement
# Indentation is four (4) spaces.
if True:
    print("It is true")

print("Done")

if "eggs":
    print("yes, why not")

# Flat is better than nested
h = 42
if h > 50:
    print("greater than 50")
    if h > 100:
        print("Greater than 100")
elif h < 50: #Else IF
    print("Less than 50")
else:
    print("Equals 50")

print("Done")