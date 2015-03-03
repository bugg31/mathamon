#!/usr/bin/env python

#Imports
from random import randint
from random import random
from random import uniform
from fractions import Fraction

#constants

MAX_DECIMAL_PLACES = 3
MIN_DECIMAL_PLACES = 1

FRACTION_PLACES = 1

MIN_MULTIPLICAND = 1
MAX_MULTIPLICAND = 100

ADDITION = 1
SUBTRACTION = 2
MULTIPLICATION = 3
DIVISION = 4

#area variables
main_menu_area = 1
helping = 0
asking = 0
level1 = 0
level2 = 0
level3 = 0
level4 = 0
level5 = 0
raw_imputing = 1

# Main Menu
def main_menu():
	print("Hello and welcome to Mathamon!")
	print("Just type in your answer to everything and yeah...")
	if raw_imputing == 1:
		next_area = raw_input("Do You want to 'Play' or 'Get Help'")
		global raw_imputing = 0
		next_area.lowercase

	if next_area == "play":
		global main_menu_area = false
		return next_area
	elif next_area == "get help":
		global main_menu_area = false
		return next_area
	else:
		print("That is not valid.")
		global raw_imputing = 1

# help (printing the controls)

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

def fraction_maker():
	decimal_1 = randint(1, 10)
	decimal_2 = randint(1, 10)
	decimal_3 = randint(1, 10)
	decimal_4 = randint(1, 10)
	fraction_1 = Fraction(decimal_1, decimal_3)
	fraction_2 = Fraction(decimal_2, decimal_4)
	return (fraction_1, fraction_2)

# running
if __name__ == '__main__':
	if asking == 1:

		question_type = 129
		if question_type == MULTIPLICATION:
			multiplicand, multiplier, answer = multiplication_maker()
			print("{} * {} = {}".format(multiplicand, multiplier, answer))
		elif question_type == DIVISION:
			dividend, divisor, quotient = division_maker()
			print("{} / {} = {}".format(dividend, divisor, quotient))
		elif question_type == ADDITION:
			fraction_1, fraction_2 = fraction_maker()
			answer = fraction_1 + fraction_2
			print("{} + {} = {}".format(fraction_1, fraction_2, answer))
		elif question_type == SUBTRACTION:
			fraction_1, fraction_2 = fraction_maker()
			answer = fraction_1 - fraction_2
			print("{} - {} = {}".format(fraction_1, fraction_2, answer))
		else:
			print("Question type {} not implemented yet!".format(question_type))
	elif main_menu_area == 1:
		main_menu()
