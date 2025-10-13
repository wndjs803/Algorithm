import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        List<Integer> array = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            array.add(num_list[i]);
        }
        
        return array.stream()
                    .mapToInt(Integer::intValue)
                    .toArray();
    }
}