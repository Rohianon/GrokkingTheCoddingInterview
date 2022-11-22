def non_repeat_substring(str1):
    window_start, max_length = 0, 0
    char_index_map = {}

    for window_end in range(len(str1)):
        right_char = str1[window_end]

        if right_char in char_index_map:
            """
            in the current window, we will not have any 'right_char' after
            it's previous index and if window_start is already ahead of the last  index of
            right_char, we'll keep window_start
            """
            window_start = max(window_start, char_index_map[right_char] + 1)

        # insert the right_char into the map
        char_index_map[right_char] = window_end
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length, str1[window_start:window_end];

def main():
    print("Length of the longest substring: " +
          str(non_repeat_substring("aabccbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abbbb")))
    print("Length of the longest substring: " +
          str(non_repeat_substring("abccde")))


main()
