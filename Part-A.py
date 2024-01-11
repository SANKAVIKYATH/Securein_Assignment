#part_A 1.
total_combinations = 6 * 6
print("Total Combinations:", total_combinations)

#part_A 2.
distribution_matrix = [[0] * 6 for i in range(6)]

for i in range(1, 7):
    for j in range(1, 7):
        distribution_matrix[i-1][j-1] = (i, j)

# Display the distribution matrix
for row in distribution_matrix:
    print(row)

#part_A 3.
probability_matrix = [[0] * 6 for j in range(6)]

for i in range(6):
    for j in range(6):
        probability_matrix[i][j] = 1 / total_combinations

# Display the probability matrix
for row in probability_matrix:
    print(row)

