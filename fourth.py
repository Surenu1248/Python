# 4.	Given a list of non-empty tuples, return a list sorted in increasing order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


lst = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]


def my_sort(a):
    return sorted(a, key=lambda x: x[1])


print(my_sort(lst))
