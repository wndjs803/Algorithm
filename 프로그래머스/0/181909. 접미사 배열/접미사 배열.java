import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> list = new ArrayList<>();
        int start = 0;
        
        while (start < my_string.length()) {
            list.add(my_string.substring(start, my_string.length()));
            start++;
        }
        Collections.sort(list);
        return list.toArray(new String[0]);
    }
}