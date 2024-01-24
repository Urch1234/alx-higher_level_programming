#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Use the map function to create new list by appling a
     lmbda function that replaces 'search' with 'replace' for
     each element in the my_list
     new_list = list(map(lambda n: replace if n == search else n, my_list))
     return (new_list)
   """
    new_list = list(map(lambda n: replace if n == search else n, my_list))
    return (new_list)
