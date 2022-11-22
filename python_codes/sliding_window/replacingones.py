from typing import List;
def replacing_ones(arr: List[int], k: int) -> int:
    max_len, window_start, max_ones_count = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1

        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start +=1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len
def main():
    print(replacing_ones([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(replacing_ones([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

if __name__ == "__main__":
    main()
