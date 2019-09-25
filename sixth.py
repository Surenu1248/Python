# 6.Write a function to print the information in the dictionary(bookstore) in the given format
# bookstore={"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":
# ["Harry Potter”, J K. Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
"""BOOKSTORE
['Learning XML', 'Erik T. Ray', '2003', '39.95']
['Everyday Italian', 'Giada De Laurent is', '2005', '30.00']
 ['Harry Potter', 'J K. Rowling', '2005', '29.99']
"""
bookstore = dict({"New Arrivals": {"COOKING": ["Everyday Italian", "Giada De Laurentiis", "2005", "30.00"],
                                   "CHILDREN": ["Harry Potter”, J K. Rowling", "2005", "29.99"],
                                   "WEB": ["Learning XML", "Erik T. Ray", "2003", "39.95"]}})

final = ["BOOKSTORE"]


def information(inf):
    final.append(bookstore["New Arrivals"]["WEB"])
    final.append(bookstore["New Arrivals"]["COOKING"])
    final.append(bookstore["New Arrivals"]["CHILDREN"])

    return final


print(*information(bookstore), sep='\n')
