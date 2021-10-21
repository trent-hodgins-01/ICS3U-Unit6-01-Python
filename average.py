# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/21/2021
# This is the Average program
# The program generates and displays 10 random numbers between 1-100
# The program then calculates and displays the average of all the numbers


import random


def main():
    # this function uses an array

    average = []
    answer = 0
    added_numbers = 0

    # input
    for loop_counter in range(0, 10):
        a_number = random.randint(1, 100)
        average.append(a_number)
        print("The random nuber is {0}".format(a_number))
        added_numbers = added_numbers + a_number

    answer = added_numbers / 10

    print("\nThe average is {0}".format(answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
