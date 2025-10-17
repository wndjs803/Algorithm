class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] query : queries) {
            int first = query[0];
            int second = query[1];
            
            int temp = arr[first];
            arr[first] = arr[second];
            arr[second] = temp;
        }
        
        return arr;
    }
}