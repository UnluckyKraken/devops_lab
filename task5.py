n = int(input())
matrix = list()
row = list()

for i in range(n):
    row_str = input()
    row = row_str.split()
    matrix.append(row)

first_diagonal = sum([int(matrix[i][i]) for i in range(n)])
second_diagonal = sum([int(matrix[i][n - i - 1]) for i in range(n)])

print(abs(first_diagonal - second_diagonal))
