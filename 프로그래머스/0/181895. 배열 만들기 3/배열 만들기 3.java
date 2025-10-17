import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> list = new ArrayList<>();
        
        for (int[] interval : intervals) {
            int first = interval[0];
            int second = interval[1];
            
            for (int i = first; i <= second; i++) {
                list.add(arr[i]);
            }
        }
        
        return list.stream()
                   .mapToInt(Integer::intValue)
                   .toArray();
    }
}