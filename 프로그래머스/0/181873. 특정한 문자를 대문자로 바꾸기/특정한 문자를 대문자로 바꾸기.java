import java.util.*;

class Solution {
    public String solution(String my_string, String alp) {
        List<String> array = new ArrayList<>();
        
        for(String s : my_string.split("")) {
            if (s.equals(alp)) array.add(s.toUpperCase());
            else array.add(s);
        }
        
        return String.join("", array);
    }
}