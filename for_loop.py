"""
Practice for loops
Keyword: for
"""

cities = ["London", "New York", "Madrid", "Paris", "Ogden"]
# iterate over a list
for city in cities:
    print (city)
# iterate over a dictionary
d = {'alice':'801-123-4567',
     'pedro': '956-445-78-8966',
     'john':'651-321-66-4477'}
for item in d:
    print(item, "=>", d[item])

