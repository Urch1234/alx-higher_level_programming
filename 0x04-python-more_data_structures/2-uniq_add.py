#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum_of_uniq = sum(list(uniq_list))
    return sum_of_uniq
