# python-practice
Emmanuel Kipkirui
184697


1. Sum All Elements in a List 
Goal: Add up all the numbers in a list.

Approach: Start with a total of 0, then loop through each number and keep adding it to the total.

Why: A simple loop helps us visit each element exactly once and keep track of the sum.

2. Check if a Number is Even or Odd
Goal: Determine if a number is even or odd.

Approach: Use the modulus operator %. If number % 2 == 0, it’s even; otherwise, it’s odd.

Why: The modulus operator is the quickest way to check divisibility by 2.

3. Compute Factorial Using a Loop 
Goal: Find the factorial of a number (e.g., 5! = 5×4×3×2×1).

Approach: Use a loop that multiplies all integers from 1 to n.

Why: Loops provide an easy way to accumulate a product step-by-step.

4. Reverse a String Without Built-in Methods 
Goal: Reverse the letters in a string manually.

Approach: Loop through the string and keep adding each new character to the front of a new string.

Why: By putting each character before the existing ones, we reverse the order naturally.

5. Compute Factorial Using Recursion 
Goal: Find the factorial using recursion (a function calling itself).

Approach: Define the factorial of n as n * factorial(n-1) with a base case when n is 0 or 1.

Why: Recursion breaks a big problem into smaller ones, following the mathematical definition of factorial.

6. Sum of Digits of a Number 
Goal: Add all the digits in a number together.

Approach: Use modulus % to pick off the last digit and integer division // to remove it, repeating until the number becomes 0.

Why: It's an efficient way to isolate and process each digit without converting to a string.
