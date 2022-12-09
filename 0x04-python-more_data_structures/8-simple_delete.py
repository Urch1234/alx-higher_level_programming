#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is not None:
        del a_dictinary[key]
    return (a_dictionary)
