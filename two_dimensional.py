#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Dec 2019
# This is program average calculator out of two-dimensional list

import random


def average(a_list):
    # This calculates average of all integer items in a two-dimensional list

    # process
    for row in a_list:
        for number in row:
            total =+ number
            items =+ 1

    # Calculates average
    average = total / items

    # output
    return average


def main():
    # This creates a two-dimensional list based on user input, fills it with
    #    random numbers from -50

    # This is a list to hold the 20 numbers
    numbers = []
    final_average = 0

    # This welcomes user
    print("I make two-dimensional list/array for you.\n")

    # input
    row = int(input("give me row amount: "))
    column = int(input("give me column amount: "))

    # process
    for repeater in range(0, row):
        inside_array = []
        for number in range(0, column):
            inside_array.append(2)
        numbers.append(inside_array)

    final_average = average(numbers)
    print("\nThe average is " + str(final_average))


if __name__ == "__main__":
    main()
