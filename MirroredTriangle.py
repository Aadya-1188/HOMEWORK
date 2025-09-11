# Number of rows in the triangle
rows = 5

# Loop to print the mirrored right-angled triangle
for i in range(1, rows + 1):

    # Print spaces first

    print(" " * (rows - i) + "*" * i)
