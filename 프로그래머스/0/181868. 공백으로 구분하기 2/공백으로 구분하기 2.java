import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        List<String> list = new ArrayList<>();
        
        for (String s : my_string.split(" ")) {
            if (!s.equals("")) list.add(s);
        }
        
        return list.toArray(new String[list.size()]);
    }
}