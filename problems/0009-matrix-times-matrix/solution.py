def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if not a or not b or len(a[0]) != len(b):
        return -1

    a_rows = len(a)
    a_cols = len(a[0])
    b_rows = len(b)
    b_cols = len(b[0])

    result = [
        [0 for _ in range(b_cols)] for _ in range(a_rows)
    ]

    for i in range(a_rows):
        for j in range(b_cols):
            dot_product = 0

            for k in range(a_cols):
                dot_product += a[i][k] * b[k][j]

            result[i][j] = dot_product

    return result