# map() , filter() , reduce()


numbers = [1, 2, 3]


def double(a):
    return a * 2


res = map(double, numbers)


print(list(res))
