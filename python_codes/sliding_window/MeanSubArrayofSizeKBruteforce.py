def find_averages(k, arr):
	result = []
	for i in range(0, len(arr)-k+1):
		# find the smu of the next 'k' elements
		buf = 0.0
		_sum = [buf := buf + arr[j] for j in range(i, i+k)]
		print(_sum)
		# average
		result.append(_sum[-1]/k)
	return result

def main():
	result = find_averages(5, [1,3,2,6,-1,4,1,8,2])
	print("Averages of subarrays of size k: ", str(result))





if __name__ == "__main__":
	main()
