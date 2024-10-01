"""
Description: Demonstrates how to handle exceptions.
Author: Damien Altenburg
Date: 2023-10-1
Usage: python guessing_game.py
"""
from random import randint

LOW_RANGE = 1
HIGH_RANGE = 10

NUMBER_OF_JELLYBEANS = randint(LOW_RANGE, HIGH_RANGE)

guess = 0
guess_count = 0
valid_guess_values = range(LOW_RANGE, HIGH_RANGE + 1)
