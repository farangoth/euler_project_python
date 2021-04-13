import functions as fct

rangemax = 1000
max_n_triangle = 0
max_triangles = []
for p in range(1, rangemax):
    triangles = []
    for a in range(1, p):
        for b in range(a, p - a):
            c = p - (a + b)
            if not (fct.is_pythagorean(a, b, c)):
                continue
            else:
                triangles.append([a, b, c])
                if len(triangles) > max_n_triangle:
                    max_triangles = triangles.copy()
                    max_n_triangle = len(max_triangles)

print(max_n_triangle, "for the perimeter", sum(max_triangles[0]))
for triangle in max_triangles:
    print(triangle)
