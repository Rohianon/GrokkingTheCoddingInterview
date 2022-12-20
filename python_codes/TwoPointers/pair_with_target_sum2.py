def pair_with_target_sum(arr, target):
    nums = {} #store numbers and their indices
    for i, num in enumerate(arr):
    if target - num in nums:
        return [nums[target - num], i]
    else:
        nums[arr[i] = i
    return [-1, -1]


def main():
  print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
  print(pair_with_target_sum([2, 5, 9, 11], 11))


main()
