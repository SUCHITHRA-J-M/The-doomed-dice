import itertools
total_combinations = 36
combinations_matrix = [[0] * 6 for _ in range(6)]

for i in range(6):
    for j in range(6):
        combinations_matrix[i][j] = (i + 1) + (j + 1)

print("Combinations Matrix:")
for row in combinations_matrix:
    print(row)


print("\nProbability of Sums:")
for i in range(2, 13):
    sum_count = sum(1 for row in combinations_matrix for num in row if num == i)
    probability = sum_count / total_combinations
    print(f"P(Sum = {i}) = {probability}")


def undoom_dice(die_a, die_b):
   
    new_die_a = [min(num, 4) for num in die_a]

    new_die_b = die_b

    return new_die_a, new_die_b

initial_die_a = [1, 2, 3, 4, 5, 6]
initial_die_b = [1, 2, 3, 4, 5, 6]

new_die_a, new_die_b = undoom_dice(initial_die_a, initial_die_b)

print("\nTransformed Dice:")
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
