package slidingwindow;

public class LongestSubarrayOf1sAfterDeletingOneElement {
    public static int findLength(int[] arr) {
        int maxLength = 0, windowStart = 0, max_ones_count = 0;

        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            if (arr[windowEnd] == 1) max_ones_count++;

            if ((windowEnd - windowStart + 1 - max_ones_count) > 1) {
                if (arr[windowStart] == 1) max_ones_count--;
                windowStart++;
            }

            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);

        }
        return maxLength - 1;
    }

    public static void main(String[] args) {
        System.out.println(
                LongestSubarrayOf1sAfterDeletingOneElement.findLength(new int[]{0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1}));
        System.out.println(
                LongestSubarrayOf1sAfterDeletingOneElement.findLength(new int[]{0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1}));
    }
}
