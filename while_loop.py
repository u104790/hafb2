"""
Lear Conditional Repetition
Two loops: for-loops and while-loops
"""

counter = 5
while counter != 0:
    print(counter)
    # Augmented Operator
    counter -= 1                # or counter = counter - 1
print("")
counter = 5
while counter:
    print(counter)
    # Augmented Operator
    counter -= 1                # or counter = counter - 1

# Run forever
while True:
    print("Enter a number")
    response = input()          # take user input
    if int(response) % 7 == 0:  # number divisible by 7
        break                   # Exit loop

print("outside while loop")