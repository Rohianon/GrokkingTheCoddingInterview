from typing import List


def sortArray(nums: List[int]) -> List[int]:

    n = len(nums)

    if n < 2:
        return nums  # list is already sorted

    # Divide
    mid = n//2

    s1 = nums[0:mid]
    s2 = nums[mid:n]

    # conquer using recursion
    sortArray(s1)
    sortArray(s2)

    # result
    merge(s1, s2, nums)
    return nums


def merge(s1: List[int], s2: List[int], S: List[int]) -> None:
    i = j = 0
    while i + j < len(S):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            S[i + j] = s1[i]
            i += 1
        else:
            S[i+j] = s2[j]
            j += 1


if __name__ == "__main__":
    a = [5, 2, 3, 1]
    b = [5, 1, 1, 2, 0, 0]
    c = [0]
    sortArray(a)
    sortArray(b)
    sortArray(c)
    print(a)
    print(b)
    print(c)
