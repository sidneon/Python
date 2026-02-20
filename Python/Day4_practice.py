#1. Write a program to reverse a list and remove duplicate using set

#method 1

lst = ["apple", "orange", "apple", "banana", 1, 5, "cherry"]

unique_items = set(lst)

print(unique_items)

reverse_lst = list(unique_items)[::-1]
print(reverse_lst)

#Method 2

def list_set(n):
    seen = set()
    unique_items = []

    for item in lst:
        if item not in seen:
            unique_items.append(item)
            seen.add(item)
    return unique_items[::-1]

lst = ["apple", "orange", "apple", "banana", 1, 5, "cherry"]
print(list_set(lst))

#2. Create a program that stores student grades in a dictionarry and calculates the average grades.abs

students = {}

def add_or_update_grades():
    name = input("Enter student name: ")
    