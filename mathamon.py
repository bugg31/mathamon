#!/usr/bin/env python

#Imports
from random import randint
from random import random

# main menu function


# help (printing the controls)


# Questions

# 10 * 0.1
# 10 * 0.001
# 100 * 0.981

# 9 * 0.4
# 2 * 0.274
# 1 * 0.283
# 3 * 1.3
# 27 * 0.4

# division: special case of multiplication so we get nice numbers


# 1/2 + 3/4
# 1/7 + 4/8
# 2 10/200 + 9 138/200

def choose_integer():
	return randint(1, 100)


def choose_float():
	return round(random(),3)


if __name__ == '__main__':
	print(choose_integer())
	print(choose_float())

