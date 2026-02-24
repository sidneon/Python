import re

#1. Write a program to count the number of vowels in a string

def count_vowels(v):
    vowels = "aeiou"
    count = 0
    lower = v.lower()
    for char in lower:
        if char in vowels:
            count += 1
    return count

print(f"{count_vowels("HeEllo")}")

#Q1. Creatae a program to find and replace all email address in a text using regex

def replace_email(text, replacement="Email"):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    result = re.sub(email_pattern, replacement, text)

    return result

sample = '''Hello John, you can contact me at jane.doe@example.com for the project details.
If you need support, please email support@company.org or sales@company.org.'''

replaced_sample = replace_email(sample)

print(replaced_sample)


#Q3. Write a program to reverse a word in a sentence (not letter)

def reverse_sentence(sentence):

    words = sentence.split()
    reverse_word = words[::-1]
    reverse_sentence = ' '.join(reverse_word)

    return reverse_sentence

sentences = input("Enter a sentence: ")

print(f"revese sentece for {sentences} : {reverse_sentence(sentences)}")





