import java.util.*;

class Solution {
    public String solution(String str1, String str2) {
        List<String> array = new ArrayList<>();
        String[] str1List = str1.split("");
        String[] str2List = str2.split("");
        
        for (int i = 0; i < str1.length(); i++) {
            array.add(str1List[i]);
            array.add(str2List[i]);
        }
        
        return String.join("", array);
    }
}