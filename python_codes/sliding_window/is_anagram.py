def is_anagram(str1: str, str2: str) -> bool:
    if len(str1) != len(str2): return False
    str1_map = {}
    for chr in str1:
        str1_map[chr] = 1 + str1_map.get(chr, 0)

    str2_map = {}
    for chr in str2:
        if chr not in str1_map:
            return False
        else:
            str2_map[chr] = 1 + str2_map.get(chr, 0)
    return str1_map == str2_map

def main():
    print(f'The strings are ')

if __name__ == "__main__":
    main()
