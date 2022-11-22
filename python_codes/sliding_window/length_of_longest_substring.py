def length_of_longest_substring(str1:str, k:int) -> int:
    max_length, max_repeat_letter_count, window_start = 0,0,0
    frequency_map = {}

    for window_end in range(len(str1)):
        frequency_map[str1[window_end]] = 1 + frequency_map.get(str1[window_end], 0)

        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[str1[window_end]]);

        # shrink whenever the replacements to make are greater than k
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = str1[window_start];
            frequency_map[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
if __name__ == "__main__":
    main()
