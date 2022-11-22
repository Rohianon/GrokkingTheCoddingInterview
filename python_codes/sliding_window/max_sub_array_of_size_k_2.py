from typing import List

def max_sub_array_of_size_k(k:int, arr:List[int]) -> float:
	window_sum, max_sum = 0, 0
	window_start = 0

	for window_end in range(len(arr)):
		window_sum += arr[window_end]
		print("Window Sum at ",window_end,window_sum)
		if window_end >= k -1:
			max_sum = max(window_sum,  max_sum)
			print("Max Sum",max_sum)
			window_sum -= arr[window_start]
			print("window sum",window_sum)
			window_start += 1 # slide the window
			print("window start",window_start)
	return max_sum, window_sum, window_start


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
