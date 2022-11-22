def find_permutation(str1:str, pattern:str) -> boolean:
    matches, window_start = 0, 0
    charFrequencyMap = {}

    # fill the charMap with the characters in the pattern
    for chr in pattern:
        charFrequencyMap[chr] = charFrequencyMap.get(chr, 0) + 1

    # extend the window [window_start, window_end]
    for window_end in range(len(str1):
        right_char = str1[window_end]
        if right_char in charFrequencyMap:
            charFrequencyMap[right_char] -= 1
            if charFrequencyMap[right_char] == 0:
                matches -= 1
            window_start += 1


    if matches == len(charFrequencyMap):
        return True

    # shrink window
    while window_end > len(pattern) - 1:
        left_char = str1[window_start]
        window_start += 1
        if left_char in charFrequencyMap:
            if charFrequencyMap[left_char] == 0:
                matches -= 1
            charFrequencyMap[left_arr] -= 1
           

    return False
