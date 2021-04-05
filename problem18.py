"""Find the maximum total from top to bottom
of the triangle in triangle18.txt."""

import functions

with open("p018_triangle.txt", "r") as f:
    triangle = [[int(num) for num in line.split(" ")] for line in f]

solution18 = functions.best_sum(triangle)
print("Sol18: ", solution18)
