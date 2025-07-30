import math

# 9. Prime Number
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 10. Sum of Digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 11. LCM and GCD
def gcd_and_lcm(a, b):
    gcd_val = math.gcd(a, b)
    lcm_val = abs(a * b) // gcd_val
    return lcm_val, gcd_val

# 12. List Reversal
def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

# 13. Sort a List (Bubble Sort)
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# 14. Remove Duplicates
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# 15. String Length
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# 16. Count Vowels and Consonants
def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# Menu Interface
def main():
    while True:
        print("\nSelect an option:")
        print("9. Check Prime Number")
        print("10. Sum of Digits")
        print("11. LCM and GCD")
        print("12. Reverse List")
        print("13. Sort List")
        print("14. Remove Duplicates")
        print("15. String Length")
        print("16. Count Vowels and Consonants")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "9":
            n = int(input("Enter an integer: "))
            print("Prime:", is_prime(n))
        elif choice == "10":
            n = int(input("Enter an integer: "))
            print("Sum of digits:", sum_of_digits(n))
        elif choice == "11":
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            lcm, gcd = gcd_and_lcm(a, b)
            print("LCM:", lcm)
            print("GCD:", gcd)
        elif choice == "12":
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            print("Reversed list:", reverse_list(lst))
        elif choice == "13":
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            print("Sorted list:", sort_list(lst))
        elif choice == "14":
            lst = list(map(int, input("Enter list elements separated by space: ").split()))
            print("List without duplicates:", remove_duplicates(lst))
        elif choice == "15":
            s = input("Enter a string: ")
            print("Length of string:", string_length(s))
        elif choice == "16":
            s = input("Enter a string: ")
            vowels, consonants = count_vowels_consonants(s)
            print("Vowels:", vowels)
            print("Consonants:", consonants)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
