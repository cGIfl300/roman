#!/usr/bin/env python3

import argparse


class Roman:
    """
    Get a digit, return a string in self.
    digit: int, the integer to convert
    """

    def __init__(self, digit=0):
        self.digit = digit
        self.roman = ""
        self.values = [[1000, "M"],
                       [900, "CM"],
                       [500, "D"],
                       [400, "CD"],
                       [100, "C"],
                       [90, "XC"],
                       [50, "L"],
                       [40, "XL"],
                       [10, "X"],
                       [9, "IX"],
                       [5, "V"],
                       [4, "IV"],
                       [1, "I"]]
        self.convert(digit=self.digit)

    def convert(self, digit):
        # Convert a digit into roman string
        try:
            digit = int(self.digit)
        except TypeError:
            raise TypeError("self.digit must be an integer")
        if digit < 1:
            raise ValueError("self.digit must be an integer greater than 1")
        digit = digit + 1
        to_return = ""
        for val in self.values:
            while digit > val[0]:
                to_return = to_return + val[1]
                digit = digit - val[0]
        self.roman = to_return


if __name__ == '__main__':
    to_try = 0
    # Add arguments management
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--convert",
        help="convert a digit into roman ie: main.py"
             " --convert 16 will return XVI"
    )
    args = parser.parse_args()

    # Test input
    if args.convert:
        # Instance the main Class
        app = Roman(digit=args.convert)
        print(app.roman)
