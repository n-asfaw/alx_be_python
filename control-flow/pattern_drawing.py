size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    # Use a for loop for columns in the current row
    for col in range(size):
        print("*", end="")  # Print asterisks without newline
    print()  # Move to the next line after the row is complete
    row += 1

