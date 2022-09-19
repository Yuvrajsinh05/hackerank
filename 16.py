#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve():
    # Write your code here

    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    tip=float((meal_cost*tip_percent)/100)
    tax=float((meal_cost*tax_percent)/100)
    total_cost=round(meal_cost+tip+tax)
    print(total_cost)
solve()

    