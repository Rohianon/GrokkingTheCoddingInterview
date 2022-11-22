def max_sub_array_of_size_k(k, arr):
	window_sum = sum(arr[:k])
	max_sum = window_sum

	for window_set in range(k, len(arr)):
		max_sum = max(max_sum, window_sum)
		window_sum += arr[window_set] - arr[window_set - k]
	return max_sum

def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

if __name__ == "__main__": main()
