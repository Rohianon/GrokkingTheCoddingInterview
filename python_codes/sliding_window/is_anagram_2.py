def is_anagram(s: str, t:str):
    import collections
    return collections.Counter(s) == collections.Counter(t)


def main():
    s = "anagram"
    t = "nagaram"
    print(f"Is {t} and {s} anagrams?", is_anagram(s, t))
    s = "rat"; t = "car"
    print(f"Is {t} and {s} anagrams?", is_anagram(s, t))


if __name__ == "__main__":
    main()
