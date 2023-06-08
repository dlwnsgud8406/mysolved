def count_ways(m, n):
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i + j == 10:
                count += 1
    return count

# Prompt the user for input
m = int(input())
n = int(input())

# Calculate the number of ways to get a sum of 10
num_ways = count_ways(m, n)

# Print the result
if num_ways == 1:
    print("There is 1 way to get the sum 10.")
else:
    print("There are", num_ways, "ways to get the sum 10.")
