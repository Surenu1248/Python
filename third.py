# 3.Given a list of strings, return a list with the strings in sorted order, except group all the strings that begin
# with 'x' first. e.g. ['mix', 'xyz','apple','xanadu','aardvark'] yields ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

a = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
c = []
d = []


def my_sort(lst):
    for ab in lst:
        if ab[0] == 'x':
            c.append(ab)
        else:
            d.append(ab)
    c.sort()
    d.sort()
    return c + d


print(my_sort(a))
