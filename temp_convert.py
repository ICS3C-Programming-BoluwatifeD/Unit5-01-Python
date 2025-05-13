#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on March 31
# This program coverts from celsius to fahrenheit


def main():

    fahrenheit()


def fahrenheit():

    celsius_str = input("Enter the temperature in celsius: ")

    try:

        celsius = float(celsius_str)

        fahrenheit = 9 / 5 * celsius + 32

        print(f"{celsius} celsius is equivalent to {fahrenheit} fahrenheit")

        print("")

    except:

        print("Please enter a valid number")

    finally:

        print("You have converted celsius to fahrenheit")


if __name__ == "__main__":

    main()
