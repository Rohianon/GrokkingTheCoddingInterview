from typing import List

def smallest_subarray_sum(s: int, arr:List[int]) -> int:
	window_sum, min_length = 0, float("inf");
	window_start = 0;

	for window_end in range(len(arr)):
		# update the window sum
		window_sum += arr[window_end]

		while (window_sum >= s):
			min_length = min(min_length, window_end-window_start +1)
			# update the window sum
			window_sum -= arr[window_start]
			# shift window
			window_start += 1
	if min_length == float("inf"):
		return 0
	return min_length



def main():
	setter = "Smallest subarray length: "
	print(setter + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
	print(setter  + str(smallest_subarray_sum(7, [2, 1, 5, 2, 8])))
	print(setter +str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))


if __name__ == "__main__":
	main()
