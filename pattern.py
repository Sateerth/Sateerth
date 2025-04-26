def print_pattern():
    pattern = [
        [1, 1, 1, 1, 2],
        [3, 2, 2, 2, 2],
        [3, 3, 3, 3, 4],
        [5, 4, 4, 4, 4],
        [5, 5, 5, 5, 6]
    ]
    
    for row in pattern:
        for num in row:
            print(num, end="")
        print()

# Call the function
print_pattern()
