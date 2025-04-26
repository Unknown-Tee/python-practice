# This function takes a list and returns the sum of all its elements using a loop.
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
print(sum_list([1, 2, 3, 4]))  # Output: 10