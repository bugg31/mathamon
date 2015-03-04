#!/usr/bin/env python

# for running it without terminal
# http://www.tutorialspoint.com/execute_python_online.php 

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

def asking_loop():
	points = 0
	while True:
		question_type = choose_question_type()

		if question_type == MULTIPLICATION:
			multiplicand, multiplier, answer = multiplication_maker()
			players_answer = raw_input("{} * {} = ".format(multiplicand, multiplier))
		elif question_type == DIVISION:
			dividend, divisor, answer = division_maker()
			players_answer = raw_input("{} / {} = ".format(dividend, divisor))
		elif question_type == ADDITION:
			fraction_1, fraction_2 = fraction_maker()
			answer = fraction_1 + fraction_2
			players_answer = raw_input("{} + {} = ".format(fraction_1, fraction_2))
		elif question_type == SUBTRACTION:
			fraction_1, fraction_2 = fraction_maker()
			answer = fraction_1 - fraction_2
			players_answer = raw_input("{} - {} = ".format(fraction_1, fraction_2))
		else:
			print("Question type {} not implemented yet!".format(question_type))

		if players_answer.strip() == str(answer):
			print("CORRECT :D")
			points += 1
			print("You have {} points".format(points))
		else:
			print("You got it wrong D:")
			print("Your score was {}".format(points))
			print("The answer was {}".format(answer))
			break
# running
if __name__ == '__main__':
	print("Always have a decimal at the end so if the answer is 60, type 60.0 otherwise it bugs out")
	print("answer decimals with decimals and fractions with fractions.")
	asking_loop()