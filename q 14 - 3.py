def matrix_sum(a):
    n = len(a)  # Assuming it's a square matrix
    diagonal_sum = 0

    for i in range(n):
        row_sum = sum(a[i])
        column_sum = sum(a[j][i] for j in range(n))
        diagonal_sum += a[i][i]
        print(f"Sum of {i+1} row: {row_sum}")
        print(f"Sum of {i+1} column: {column_sum}")

    print(f"Diagonal sum: {diagonal_sum}")

# Sample matrix
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

matrix_sum(a)
