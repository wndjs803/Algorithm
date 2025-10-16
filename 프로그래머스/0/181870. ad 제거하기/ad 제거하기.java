import java.util.*;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        
        for (String s : strArr) {
            if (!s.contains("ad")) {
                answer.add(s);
            }
        }
        
        return answer.toArray(new String[answer.size()]);
    }
}