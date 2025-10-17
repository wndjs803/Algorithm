import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        List<Integer> list = new ArrayList<>();
        
        for (int[] query : queries) {
            int s = query[0];
            int e = query[1];
            int k = query[2];
            
            int min = 1000001;
            
            for (int i = s; i <= e; i++) {
                if ((arr[i] > k) && (min > arr[i])) min = arr[i];
            }
            
            if (min != 1000001) list.add(min);
            else list.add(-1);
        }
        
        return list.stream()
                   .mapToInt(Integer::intValue)
                   .toArray();
    }
}