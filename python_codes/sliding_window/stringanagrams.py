from typing import List
def find_string_anagrams(str1: str, pattern: str) -> List[int]:
    window_start, matched = 0, 0
    char_frequency = {}

    for item in pattern:
        char_frequency[item] = 1 + char_frequency.get(item, 0)

    result_indices = []
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            # Decrement the frequency of matched character
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1


    return result_indices


def main():
    fp = find_string_anagrams("ppqp", "pq")
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))

if __name__ == "__main__":
    main()
