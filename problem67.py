"""Find the maximum total from top to bottom of the triangle in triangle67.txt."""

import functions

with open("triangle_67.txt", "r") as f:
    triangle = [[int(num) for num in line.split(" ")] for line in f]
    for row in triangle:
        if len(row) != len(triangle):
            zeros = [0] * (len(triangle) - len(row))
            row.extend(zeros)

solution67 = functions.best_sum(triangle)
print("Sol67: ", solution67)
