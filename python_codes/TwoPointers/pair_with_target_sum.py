def pair_with_target_sum(arr, target):
    left, right = 0, len(arr) - 1
    while (left < right):
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        if target > curr_sum:
            left += 1 # we need a pair with a bigger sum
        else:
            right -= 1 # we need a pair with a smaller sum
    return [-1, -1]

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()


# Time complexity: O(N)
# Space Complexity: O(1)
