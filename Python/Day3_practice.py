# Write a function to check if a number is even or odd and call it with another function.

def even_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"

def print_function(p):
    result = even_odd(p)
    print(f"{p} is a {result} number")

num = int(input("Enter a no: "))
print_function(num)

'''
Q. create a module for string operations, including functions to reverse a string, count vowels and check
    for palindromes. Import it into a script and test the function
'''

def reverse_string(s):
    return s[::-1]

def remove_space(r):
    result = r.replace(" ", "")
    return result

def count_vowels(v):
    vowels = "aeiouAEIOU"
    count = 0
    for char in v:
        if char in vowels:
            count += 1
    return count

def is_palindromes(p):
    if not p:
        return True
    last_index = len(p) - 1
    line = len(p) // 2

    for i in range(line):
        if p[i] != p[last_index - i]:
            return False
    return True

