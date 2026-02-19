import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        
        for (String str : intStrs) {
            String sub = str.substring(s, s+l);
            int num = Integer.parseInt(sub);
            
            if(num > k) answer.add(num);
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}