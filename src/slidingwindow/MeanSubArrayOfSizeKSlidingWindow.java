package slidingwindow;

import java.util.Arrays;

public class MeanSubArrayOfSizeKSlidingWindow {

    public static double[] findAverages(int k, int[] arr) {

        // create the empty array of results
        double[] result = new double[arr.length - k + 1];
        // initialize the sum and the start of window
        double windowSum = 0.0;
        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            // add the next element
            windowSum += arr[windowEnd];
            // slide the window, we don't need to slide if we've not hit the
            // required window size of 'k'
            if (windowEnd >= k - 1) {
                // calculate the average
                result[windowStart] = windowSum / k;
                // subtract the element going out
                windowSum -= arr[windowStart];
                // slide the window ahead
                windowStart++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 2, 6, -1, 4, 1, 8, 2};
        double[] result = MeanSubArrayofSizeKBruteforce.findAverages(5, arr);

        System.out.println("Averages of subarrays of size k (Sliding Window Approach): " + Arrays.toString(result));
    }
}
