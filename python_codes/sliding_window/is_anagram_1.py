def is_anagram(s: str, t: str) -> bool:
    for x in string.ascii_lowercase:
        if s.count(x) != t.count(x):
            return False
    return True


