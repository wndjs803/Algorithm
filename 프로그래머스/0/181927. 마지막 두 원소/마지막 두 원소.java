import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        List<Integer> array = new ArrayList<>();
        int length = num_list.length;
        
        for (int i = 0; i < length; i++) {
            array.add(num_list[i]);
            if (i == length - 1) {
                if (num_list[length - 2] < num_list[length - 1]) {
                    array.add(num_list[length - 1] - num_list[length - 2]);
                }
                else {
                    array.add(num_list[length - 1] * 2);
                }
            }
        }
        
        return array.stream()
                    .mapToInt(Integer::intValue)
                    .toArray();
    }
}