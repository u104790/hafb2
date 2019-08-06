"""
Learn dictionaries
Dictionaries maps keys to values.
In some languages are known as associative arrays, hashes, or maps

Create them using { } containing a key-value pair.
Retrieve them by [key value]
"""
d = {'alice':'801-123-4567',
     'pedro': '956-445-78-8966',
     'john':'651-321-66-4477'}
print(d, type(d))
# Access on element
print(d['pedro'])

# Add members to the dictionary
roster = {}                   #Empty dictionary
total = 0
while total < 3:
     # get key value
     key = input ("Enter Key")
     # get value associated to key
     value = input ("Enter value")
     # add element to dictionary
     # Note: If key value exist, it will update the value
     # otherwise it will add it to the dict.
     roster[key] = value
     total += 1
# display list
print(roster)


