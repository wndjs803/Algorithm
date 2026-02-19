import java.util.*;

class Solution {
    public int[] solution(int n, int k) {
        List<Integer> list = new ArrayList<>();
        int num = k;
        while (num <= n) {
            list.add(num);
            num += k;
        }
        
        return list.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}