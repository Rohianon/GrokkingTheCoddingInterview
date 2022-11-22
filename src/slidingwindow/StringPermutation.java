package slidingwindow;

import java.util.HashMap;
import java.util.Map;

public class StringPermutation {
    public static boolean findPermutation(String str, String pattern) {
        int windowStart = 0, matched = 0;
        Map<Character, Integer> charFrequencyMap = new HashMap<>();

        for (char chr : pattern.toCharArray())
            charFrequencyMap.put(chr,
                    charFrequencyMap.getOrDefault(chr, 0) + 1);

        /**
         * The Goal is to match all the characters from the 'charFrequencyMap' 
         * with the current window and try to extend the range [windowStart, windowEnd]
         */
        for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
            char rightChar = str.charAt(windowEnd);
            if (charFrequencyMap.containsKey(rightChar)) {
                // Decrement the frequency of the matched character
                charFrequencyMap.put(rightChar,
                        charFrequencyMap.get(rightChar) - 1);
                if (charFrequencyMap.get(rightChar) == 0) // Character is completely matched
                    matched++;
            }

            if (matched == charFrequencyMap.size())
                return true;

            if (windowEnd >= pattern.length() - 1) {
                //Shrink the window by one character
                char leftChar = str.charAt(windowStart++);
                if (charFrequencyMap.containsKey(leftChar)) {
                    if (charFrequencyMap.get(leftChar) == 0)
                        matched--; // before putting the char back, decrement the matched count
                    //put the character back for matching
                    charFrequencyMap.put(leftChar, charFrequencyMap.get(leftChar) + 1);
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println("Permutation exist: "
                + StringPermutation.findPermutation("oidbcaf", "abc"));
        System.out.println("Permutation exist: "
                + StringPermutation.findPermutation("odicf", "dc"));
        System.out.println("Permutation exist: "
                + StringPermutation.findPermutation("bcdxabcdy", "bcdyabcdx"));
        System.out.println("Permutation exist: "
                + StringPermutation.findPermutation("aaacb", "abc"));
    }
}
