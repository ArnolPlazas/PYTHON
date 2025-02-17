

squares = [x**2 for x in range(1, 11)]
# print(squares)

celsius = [0, 10, 15, 20, 25, 30]
fahrenheits = [((9/5)*temp + 32) for temp in celsius]
# print(list(zip(celsius, fahrenheits)))

# even number
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
# print(even_numbers)

odd_numbers = [x for x in range(1, 11) if x % 2 != 0]
# print(odd_numbers)

matrix = [[1, 2, 3, 5], [4, 5, 6, 6], [7, 8, 9, 9]]
flattened_matrix = [num for sublist in matrix for num in sublist]
# print(flattened_matrix)


trasposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(trasposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)