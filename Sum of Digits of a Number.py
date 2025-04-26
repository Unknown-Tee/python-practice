# This function computes the sum of digits of a number.
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    return total

# Example usage
print(sum_of_digits(1234))  # Output: 10