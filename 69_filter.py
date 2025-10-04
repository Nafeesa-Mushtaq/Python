# filter() function is used to filter elements from an iterable based on a condition (a function that returns True or False).


# Example 01
def is_vowel(letter):
    return letter.lower() in "aeiou"

letters = ['a', 'b', 'e', 'x', 'i', 'o']
vowels = list(filter(is_vowel, letters))
print(vowels)

# Example 02

words = ["apple", "", "banana", "", "cherry"]

non_empty = list(filter(lambda w: w != "", words))
print(non_empty)

# Example 03
names = ["Alice", "Bob", "Angela", "Brian", "Alex"]

starts_with_a = list(filter(lambda name: name.startswith("A"), names))
print(starts_with_a)

# Example 04
nums = [-3, -2, 0, 1, 5, -1]

positives = list(filter(lambda x: x > 0, nums))
print(positives)


