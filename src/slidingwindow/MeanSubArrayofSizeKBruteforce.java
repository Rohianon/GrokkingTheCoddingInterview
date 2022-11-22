package slidingwindow;

import java.util.Arrays;

public class MeanSubArrayofSizeKBruteforce {

    public static double[] findAverages(int k, int[] arr) {

        double[] result = new double[arr.length - k + 1];

        for (int i = 0; i <= arr.length - k; i++) {
            // find sum of next 'k' elements
            double sum = 0;
            for (int j = i; j < i + k; j++)
                sum += arr[j];
            result[i] = sum / k; //calculating the average
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 2, 6, -1, 4, 1, 8, 2};
        double[] result = MeanSubArrayofSizeKBruteforce.findAverages(5, arr);

        System.out.println("Averages of subarrays of size k: " + Arrays.toString(result));
    }
}
