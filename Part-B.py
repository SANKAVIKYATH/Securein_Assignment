def undoom_dice(die_a, die_b):
    # Calculate the original probabilities
    original_probabilities = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            original_probabilities[i][j] = 1 / 36  # Assuming 6x6 dice

    # Calculate the current probabilities based on the provided dice
    current_probabilities = [[0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            current_probabilities[i][j] = die_a[i] * die_b[j] / sum(die_a) / sum(die_b)

    # Determine the required adjustments to match the original probabilities
    adjustment_factor = [[original_probabilities[i][j] / current_probabilities[i][j] for j in range(6)] for i in range(6)]

    # Apply adjustments to the faces of new_dice_a
    new_die_a = [round(die_a[i] * adjustment_factor[i][j]) for i in range(6)]

    # Ensure that no face of new_die_a has more than 4 spots
    new_die_a = [min(4, spots) for spots in new_die_a]

    # Calculate the sum of new_die_a and any possible value of new_die_b
    new_die_b = [1, 2, 3, 4, 5, 6]

    # Adjust the probabilities of new_die_b to match the original probabilities
    adjusted_probabilities_b = [sum(current_probabilities[i][j] for j in range(6)) for i in range(6)]

    # Choose numbers for new_die_b based on adjusted probabilities
    new_die_b = [round(sum(adjusted_probabilities_b[:i+1]) * 6) for i in range(6)]
    new_die_b[-1] = 6 - sum(new_die_b[:-1])  # Adjust the last value to ensure the sum is 6

    return new_die_a, new_die_b

# Example usage
die_a = [1, 2, 3, 4, 5, 6]
die_b = [1, 2, 3, 4, 5, 6]
new_die_a, new_die_b = undoom_dice(die_a, die_b)

print("Original Die A:", die_a)
print("Original Die B:", die_b)
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
