# 2.Given a list of strings, return the count of the number of strings ,
# where the string length is 2 or more and the first and last chars of the string are the same.

a = ['axa', 'xyz', 'gg', 'x', 'yyy']
c = []


def count(b):
    for ab in a:
        if ab[0] == ab[-1] and len(ab) > 1:
            c.append(str(ab))
    return len(c)


print(count(a), end="\n")
