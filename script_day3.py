import Day3_practice

string = input("Enter a string: ")

reversed_string = Day3_practice.reverse_string(string)
vowel_count = Day3_practice.count_vowels(string)
is_palindrome = Day3_practice.is_palindromes(string)
remove_spaces = Day3_practice.remove_space(string)

#printing module function

print(f"1. reverse of {string} : {reversed_string}")
print(f"2. vowels in {string} = {vowel_count}")
print(f"3. is this palindrome -> {string} : {is_palindrome}")
print(f"4. {string} without whitespace : {remove_spaces}")
