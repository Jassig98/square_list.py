# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 10, 2022
# Description: Function that takes numbers and replaces each number with its square

def square_list(list1):
    """replaces value with its square"""
    for i in range(len(list1)):
        list1[i] = list1[i] * list1[i]
