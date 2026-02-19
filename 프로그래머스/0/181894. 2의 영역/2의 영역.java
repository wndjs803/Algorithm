import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        int start = -1;
        int end = -1;
        
        for(int i = 0; i < arr.length; i++) {
            if(start < 0 && arr[i] == 2) {
                start = i;
                continue;
            }
            
            if (arr[i] == 2) {
                end = i;
            }
        }
        
        if(start >= 0) {
            if(end > start) {
                return Arrays.copyOfRange(arr, start, end + 1);
            }
            else return Arrays.copyOfRange(arr, start, start + 1);
        }
        
        int[] answer = {-1};
        return answer;
    }
}