# 1. Sum of Two Numbers
def sum_of_two_numbers(a, b):
    return a + b

# 2. Odd or Even
def odd_or_even(number):
    return "Even" if number % 2 == 0 else "Odd"

# 3. Factorial Calculation
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 4. Fibonacci Sequence
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# 5. Reverse a String
def reverse_string(s):
    return s[::-1]

# 6. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# 7. Leap Year Check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 8. Armstrong Number
def is_armstrong_number(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n

# Test each function
if __name__ == "__main__":
    # 1. Sum
    print("1. Sum of 3 and 5:", sum_of_two_numbers(3, 5))

    # 2. Odd or Even
    print("2. 4 is:", odd_or_even(4))

    # 3. Factorial of 5
    print("3. Factorial of 5:", factorial(5))

    # 4. First 7 Fibonacci numbers
    print("4. First 7 Fibonacci numbers:", fibonacci(7))

    # 5. Reverse string "hello"
    print('5. Reverse of "hello":', reverse_string("hello"))

    # 6. Is "radar" a palindrome?
    print('6. Is "radar" a palindrome?:', is_palindrome("radar"))

    # 7. Is 2024 a leap year?
    print("7. Is 2024 a leap year?:", is_leap_year(2024))

    # 8. Is 153 an Armstrong number?
    print("8. Is 153 an Armstrong number?:", is_armstrong_number(153))
