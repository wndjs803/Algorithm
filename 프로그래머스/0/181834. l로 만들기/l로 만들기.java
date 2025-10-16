import java.util.*;

class Solution {
    public String solution(String myString) {
        List<String> list = new ArrayList<>();
        String[] myStringArray = myString.split("");
        
        for (int i = 0; i < myString.length(); i++) {
            if ((int)myString.charAt(i) < 108) {
                list.add("l");
            }
            else list.add(myStringArray[i]);
        }
        
        return String.join("", list);
    }
}