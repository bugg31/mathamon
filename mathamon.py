#!/usr/bin/env python

#Imports
from random import randint
from random import random
from random import uniform

# main menu function


#constants

MAX_DECIMAL_PLACES = 3
MIN_DECIMAL_PLACES = 1

MIN_MULTIPLICAND = 1
MAX_MULTIPLICAND = 100

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4

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
	return round(uniform(0.1, 1), choose_decimal_places())

def choose_question_type():
	return randint(1, 4)

def multiplication_maker():
	multiplicand = choose_multiplicand()
	multiplier = choose_multiplier()
	answer = multiplicand * multiplier
	return (multiplicand, multiplier, answer)

def division_maker():
	quotient, divisor, dividend = multiplication_maker()
	return (dividend, divisor, quotient)


# running
if __name__ == '__main__':
	question_type = choose_question_type()
	question_type = DIVISION # TODO implement other types

	if question_type == MULTIPLICATION:
		multiplicand, multiplier, answer = multiplication_maker()
		print("{} * {} = {}".format(multiplicand, multiplier, answer))
	elif question_type == DIVISION:
		dividend, divisor, quotient = division_maker()
		print("{} / {} = {}".format(dividend, divisor, quotient))
	else:
		print("Question type {} not implemented yet!".format(question_type))

