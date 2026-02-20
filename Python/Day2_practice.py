#1. Write a program to calculate the factorial of a number using while loop

def factorial_while(n):
    if n < 0:
        return "factorial doesn't exist."
    elif n == 0:
        return 1
    else:
        x = 1
        i = 1
        while i <= n:
            x *= i
            i += 1
        return x
def print_factorial(n):
    result = factorial_while(n)
    print(f"factorial of {n} is {result} ")

in_factorial = int(input("Enter a Number: "))
print_factorial(in_factorial)

#Create a program to find the largest number in list using for loop

def largest_num(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    
    return largest


my_list = [6, 9, 45, 46, 97, 48, 32, 96]
print(f"largest number in this list is {largest_num(my_list)}")