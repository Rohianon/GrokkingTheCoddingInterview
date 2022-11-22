package slidingwindow;

import java.util.HashMap;
import java.util.Map;

public class MaxFruitCountOf2Types {
    public static int findMaxLength(char[] arr) {
        int maxLength = 0, windowStart = 0;
        Map<Character, Integer> fruitFrequencyCount = new HashMap<>();
        for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
            char right_array = arr[windowEnd];
            fruitFrequencyCount.put(right_array, fruitFrequencyCount.getOrDefault(right_array, 0) + 1);

            // Shrink the sliding window until we're left with '2' fruits in the frequency map
            while (fruitFrequencyCount.size() > 2) {
                fruitFrequencyCount.put(arr[windowStart], fruitFrequencyCount.get(arr[windowStart]) - 1);

                if (fruitFrequencyCount.get(arr[windowStart]) == 0) {
                    fruitFrequencyCount.remove(arr[windowStart]);
                }

                windowStart++; //Shrink the window
            }

            maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
        }
        return maxLength;
    }

    public static void main(String[] args) {
        System.out.println("Maximum number of fruits: " +
                MaxFruitCountOf2Types.findMaxLength(new char[]{'A', 'B', 'C', 'A', 'C'}));
        System.out.println("Maximum number of fruits: " +
                MaxFruitCountOf2Types.findMaxLength(new char[]{'A', 'B', 'C', 'B', 'B', 'C'}));
    }
}
