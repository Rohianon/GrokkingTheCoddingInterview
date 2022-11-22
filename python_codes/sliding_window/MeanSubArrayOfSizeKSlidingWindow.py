def find_averages(k: int, arr: list) -> list:
	# create an empty result list
	result = []
	# initialize the sum and the start of window
	windowSum, windowStart = 0.0, 0
	# loop through the list once
	for  windowEnd in range(len(arr)):
		
		# add the next element
		windowSum += arr[windowEnd]
		
		# slide the window, 
		# no need to slide the window if we've not hit the required window size of 'k'.
		if windowEnd >= k-1:
			# calculate the average
			result.append(windowSum/k)
			# print(result)
			# subtract the element going out
			windowSum -= arr[windowStart]
			# slide the window ahead
			windowStart += 1
	return result;


def main() -> None:
	k = int(input("Input your window size"))
	result = find_averages(k, [1, 3, 2, 6, -1, 4, 1, 8, 2])
	print("Averages of subarrays using a sliding window of size k: ",str(result))


if __name__ == "__main__":
	main()

