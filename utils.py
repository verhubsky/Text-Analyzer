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
