# map() , filter() , reduce()


# numbers = [1, 2, 3]


# def double(a): return a * 2


# res = map(double, numbers)


# print(list(res))


# numbers = [1, 2, 3]


# def isEven(n):
#     return n % 2 == 0


# res = filter(lambda n: n % 2 == 0, numbers)

# print(list(res))


# expenses = [
#     ('Dinner', 80),
#     ('Coffee', 5),
# ]

# sum = 0
# for expense in expenses:
#     sum += expense[1]
# print(sum)

# this is the long way

from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Coffee', 5),
]

sum = reduce(lambda acc, expense: acc + expense[1], expenses, 0)
print(sum)
