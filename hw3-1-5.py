# Author: ATN 9/20/21

import math

a = 1
b = 3
c = -4

root = (b ** 2) - (4 * a * c)
first_solution = (-b + root ** (1/2)) / 2 * a
second_solution = (-b - root ** (1/2)) / 2 * a
print(first_solution, second_solution)
