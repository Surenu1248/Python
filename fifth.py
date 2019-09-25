# 5.Given a list of numbers, return a list where all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or modify the passed in list.

s = [1, 2, 2, 3]
b = []


def remove_dup(c):
    for a in c:
        if a not in b:
            b.append(a)
    return b


print(remove_dup(s))