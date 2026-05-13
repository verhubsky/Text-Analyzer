import sys

from utils import count_words, count_unique_words, search_top, search_the_longest_word, calculate_average_word_length

words = input("Enter words, for ex. 'I love cookies'\n>>> ")

# (!!!)
if not words:
    print('No words entered.')
    sys.exit()

# Screen
line = "-" * 23
print(line)
print('| Text-Analyzer v0.1  |')
print(line)

# 1. (& 5.) Count how many times each word appears
print("1) Words:", count_words(words))

# 2. Count how many unique words we have
print("2) Unique:", count_unique_words(words))

# 3. Creating table of Top-5 words
i = 0
print("3) Top-5:")
for i, value in enumerate(search_top(words)):
    print(f" {i + 1}. {value[0]} ({value[1]})")

# 4. Searching for longest word
print("4) Longest:", search_the_longest_word(words))

# 5. Calculating average word length
print("5) Average length:", calculate_average_word_length(words))
