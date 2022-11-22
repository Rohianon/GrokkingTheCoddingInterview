from typing import List

def longest_substring_with_k_distinct(str1:str, k:int) -> int:
    window_start, max_length = 0, 0
    char_frequency = {}

    # In the following loop, we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        print("Window end: ", window_end)
        right_char = str1[window_end]
        print("right char: ",right_char)
        char_frequency[right_char] = 1 + char_frequency.get(right_char, 0)
        print(f'Char Frequency: ',char_frequency)

        # Shrink the sliding window, until we're left with k distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            print(f'Left char: {left_char}')
            char_frequency[left_char] -= 1
            print("Char frequency: ", char_frequency)
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1 # shrink the window
            print("Window start: ", window_start)
        # remember the maximum length so far.
        max_length = max(max_length, window_end-window_start + 1)
        print("Max Length: ", max_length,"vs \t\t" f"{window_end} '-'  {window_start} + 1 = ", window_end-window_start + 1)
        print("Max_length: ", max_length)
    return max_length

def main():
    #print("Length of the longest substring: "
      #        + str(longest_substring_with_k_distinct("araaci", 2)))
    #print(f"Length of the longest substring: {longest_substring_with_k_distinct('Rohi is here', 3)}")
    print(f'Length of the longest substring: {longest_substring_with_k_distinct("cbbebi", 3)}')

if __name__ == "__main__":
    main()
