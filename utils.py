def count_words(user_input: str) -> int:
    words = user_input.strip().split()
    return len(words)


def count_unique_words(user_input: str) -> int:
    words = user_input.strip().split()
    unique_words = set(words)

    return len(set(unique_words))


def search_top(user_input: str) -> list[tuple[str, int]]:
    seen = {}
    result = []
    words = user_input.strip().split()

    for word in words:
        if word not in seen:
            seen[word] = 1
        else:
            seen[word] += 1

    i = 0
    for k, v in sorted(seen.items(), key=lambda item: item[1], reverse=True):
        i += 1
        result.append((k, v))

        if i == 5:
            break

    return result


def search_the_longest_word(user_input: str) -> str:
    words = user_input.strip().split()
    unique_words = set(words)

    return max(unique_words, key=len)


def calculate_average_word_length(user_input: str) -> int:
    avg_length_list = []
    words = user_input.strip().split()

    for word in words:
        avg_length_list.append(len(word))

    return int(sum(avg_length_list) / len(avg_length_list))


def startup(words: str):
    if not words:
        print('No words entered.')
        return

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
