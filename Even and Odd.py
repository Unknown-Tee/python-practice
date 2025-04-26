# This function checks if a number is even or odd using the modulus operator.
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example usage
print(check_even_odd(7))  # Output: Odd