#!/usr/bin/env python

#Imports
from random import randint
from random import random

# main menu function

#constants

MAX_DECIMAL_PLACES = 3
MIN_DECIMAL_PLACES = 1

MIN_MULTIPLICAND = 1
MAX_MULTIPLICAND = 100

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

# Making questions
def choose_decimal_places():
	return randint(MIN_DECIMAL_PLACES, MAX_DECIMAL_PLACES)

def choose_multiplicand():
	return randint(MIN_MULTIPLICAND, MAX_MULTIPLICAND)


def choose_multiplier():
	return round(random(), choose_decimal_places())

def choose_question_type():
	question_type = randint(1, 4)
	if question_type == 1:
		return "+"
	elif question_type == 2:
		return "-"
	elif question_type == 3:
		return "*"
	elif question_type == 4:
		return "/"

# running
if __name__ == '__main__':
	print("{} {} {}".format(choose_multiplicand(), choose_question_type(), choose_multiplier()))

