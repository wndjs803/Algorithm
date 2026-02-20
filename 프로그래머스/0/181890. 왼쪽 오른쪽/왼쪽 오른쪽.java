import java.util.*;

class Solution {
    public String[] solution(String[] str_list) {
        int index = 0;
        int direction = 0;
//         left -> -1, right -> 1
        
        for(int i = 0; i < str_list.length; i++) {
            if (str_list[i].equals("l")) {
                index = i;
                direction = -1;
                break;
            }
            
            if (str_list[i].equals("r")) {
                index = i;
                direction = 1;
                break;
            }
        }
        
        if (direction < 0) {
            return Arrays.copyOfRange(str_list, 0, index);
        }
        else return Arrays.copyOfRange(str_list, index + 1, str_list.length);
    }
}