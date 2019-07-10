#!/bin/python3

import math
import os
import random
import re
import sys


def odd(value):
    print("Weird")

def even(value):
    if value >= 2 and value < 5:
        print ("Not Weird")
    elif value > 5 and value <= 20:
        print("Weird")
    else:
        print ("Not Weird") 


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        even(n)
    else:
        odd(n)
