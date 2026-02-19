class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] arr = my_string.toCharArray();
        
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            
            int start = query[0];
            int end = query[1];
            
            while (start < end) {
                char temp = arr[start];
                arr[start] = arr[end];
                arr[end] = temp;
                start++;
                end--;
            }
        }
        
        return new String(arr);
    }
}