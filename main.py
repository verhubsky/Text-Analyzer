import sys

words = input("Enter words, for ex. 'I love cookies'\n>>> ").strip().split()

# (!!!)
if not words:
    print('No words entered.')
    sys.exit()


# 1. (& 5.) Count how many times each word appears
seen = {}
avg_length_list = []

for word in words:
    if word not in seen:
        seen[word] = 1
        avg_length_list.append(len(word))
    else:
        seen[word] += 1

print("1) Words:", len(words))


# 2. Count how many unique words we have
unique_words = list(seen.keys())
print("2) Unique words:", len(unique_words))


# 3. Creating table of Top-5 words
i = 0
print("3) Top-5 words:")
for k, v in sorted(seen.items(), key=lambda item: item[1], reverse=True):
    i += 1

    print(f" {i}. {k} ({v})")

    if i == 5:
        break


# 4. Searching for longest word
longest_word = max(unique_words, key=len)
print("4) Longest word:", longest_word)


# 5. Calculating average word length
avg_length = int(sum(avg_length_list) / len(avg_length_list))
print("5) Average word length:", avg_length)
