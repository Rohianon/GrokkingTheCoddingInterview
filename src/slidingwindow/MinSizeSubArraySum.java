package slidingwindow;

//LeetCode Question 209, 862

public class MinSizeSubArraySum {

    public static int findMinSubArray(int s, int[] arr) {
        // Declare the required variables
        int windowSum = 0, minLength = Integer.MAX_VALUE;
        int windowStart = 0;

        // Loop over our array
        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            // add the next element
            windowSum += arr[windowEnd];
            //shrink until the windowSum is smaller than s
            while (windowSum >= s) {
                minLength = Math.min(minLength, windowEnd - windowStart + 1);
                windowSum -= arr[windowStart];
                windowStart++;
            }
        }

        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }

    public static void main(String[] args) {
        int result = MinSizeSubArraySum.findMinSubArray(7, new int[]{2, 1, 5, 2, 3, 2});
        System.out.println("Smallest subarray length: " + result);
        result = MinSizeSubArraySum.findMinSubArray(7, new int[]{2, 1, 5, 2, 8});
        System.out.println("Smallest subarray length: " + result);
        result = MinSizeSubArraySum.findMinSubArray(8, new int[]{3, 4, 1, 1, 6});
        System.out.println("Smallest subarray length: " + result);
    }
}
