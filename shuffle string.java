public class Solution {
    public String restoreString(String s, int[] indices) {
        int n = s.length();
        char[] shuffled = new char[n];
        
        // Build the shuffled string based on indices
        for (int i = 0; i < n; i++) {
            shuffled[indices[i]] = s.charAt(i);
        }
        
        // Convert char array to string
        return new String(shuffled);
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example 1
        String s1 = "codeleet";
        int[] indices1 = {4, 5, 6, 7, 0, 2, 1, 3};
        System.out.println(solution.restoreString(s1, indices1)); // Output: "leetcode"
        
        // Example 2
        String s2 = "abc";
        int[] indices2 = {0, 1, 2};
        System.out.println(solution.restoreString(s2, indices2)); // Output: "abc"
    }
}
