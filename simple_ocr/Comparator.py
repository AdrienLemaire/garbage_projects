#!/usr/bin/python
# -*- coding:Utf-8 -*-

'''
File: Comparator.py
Author: Adrien Lemaire
Description: Compare an unidentified matrix to an alphabet to get its
corresponding character
'''

from numpy import *

o_dict = [
    [0, 2, 104, 205, 247, 242, 192, 76],
    [2, 170, 255, 218, 140, 148, 234, 255, 117],
    [93, 255, 182, 6, 0, 0, 21, 218, 253, 46],
    [189, 255, 34, 0, 0, 0, 0, 83, 255, 143],
    [237, 228, 0, 0, 0, 0, 0, 20, 255, 191],
    [251, 211, 0, 0, 0, 0, 0, 4, 255, 204],
    [238, 228, 0, 0, 0, 0, 0, 22, 255, 190],
    [190, 255, 35, 0, 0, 0, 0, 84, 255, 146],
    [0, 0, 0, 0, 0, 0, 20, 216, 254, 52],
    [1, 172, 255, 218, 140, 147, 233, 255, 128],
    [0, 2, 108, 207, 247, 244, 191, 77],
]

char = [
    [0, 21, 150, 227, 250, 227, 149, 19],
    [15, 218, 250, 146, 98, 147, 251, 215, 13],
    [133, 255, 96, 0, 0, 0, 100, 255, 131],
    [214, 231, 0, 0, 0, 0, 0, 232, 212],
    [247, 188, 0, 0, 0, 0, 0, 188, 246],
    [247, 188, 0, 0, 0, 0, 0, 188, 246],
    [213, 230, 0, 0, 0, 0, 0, 232, 212],
    [0, 0, 0, 0, 0, 0, 98, 255, 131],
    [15, 218, 249, 144, 98, 146, 250, 216, 13],
    [0, 21, 151, 229, 251, 228, 149, 20],
]

#print type(o_dict), type(char),"\n"


def equalize_width(my_list):
    max_width = 0
    for sublist in my_list:
        if len(sublist) > max_width:
            max_width = len(sublist)
    for sublist in my_list:
        if len(sublist) < max_width:
            sublist.extend([0] * (max_width - len(sublist)))
    return my_list

o_dict = mat(equalize_width(o_dict))
char = mat(equalize_width(char))

#print type(o_dict), type(char),"\n"

print "o_dict :", o_dict.shape, "\n", o_dict
print "char to analyze :", char.shape, "\n", char
o_dict.shape = 10, 9
print "char resized :", o_dict.shape, "\n", o_dict
#print cmp(o_dict, char)
#if o_dict == char:
    #print "equal"
