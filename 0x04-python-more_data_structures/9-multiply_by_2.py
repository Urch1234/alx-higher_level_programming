#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    double_dict = a_dictionary.copy()
    list_keys = list(double_dict.keys())

    for i in list_keys:
        double_dict[i] *= 2

    return (double_dict)
