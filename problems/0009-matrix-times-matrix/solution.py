def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]] | int:
    # Inner dimensions must match: columns of A == rows of B
    if len(a[0]) != len(b):
        return -1

    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    # Initialize result matrix C of size (rows_a x cols_b) with zeros
    c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Compute dot products
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j] += a[i][k] * b[k][j]

    return c