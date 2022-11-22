package slidingwindow;

public class FindMaxAverage {

    public static double maxAverage(int k, int[] arr) {
        double sum = 0.0;
        for (int i = 0; i < k; i++)
            sum += arr[i];
        double max = sum;
        for (int i = k; i < arr.length; i++) {
            sum += arr[i] - arr[i - k];
            max = Math.max(max, sum);
        }

        return max / k;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 2, 6, -1, 4, 1, 8, 2};
        double result = FindMaxAverage.maxAverage(5, arr);

        System.out.println("Averages of subarrays of size k (Sliding Window Approach): " + result);
    }

}
