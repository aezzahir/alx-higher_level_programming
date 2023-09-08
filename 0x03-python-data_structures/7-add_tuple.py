#!usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    n_a = len(tuple_a)
    n_b = len(tuple_b)
    for tup in [tuple_a, tuple_b]:
        if len(tup) == 0:
            sum1 += 0
        elif len(tup) == 1:
            sum1 += tup[0]
        else:
            sum1 += tup[0]
            sum2 += tup[1]
    return ((sum1, sum2))
