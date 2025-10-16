import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> intList = Arrays.stream(arr)
                                      .boxed()
                                      .collect(Collectors.toList());

        List<Integer> deleteList = Arrays.stream(delete_list)
                                      .boxed()
                                      .collect(Collectors.toList());
        
        List<Integer> answer = new ArrayList<>();
        
        for(int i = 0; i < arr.length; i++) {
            if (!deleteList.contains(intList.get(i))) {
                answer.add(intList.get(i));
            }
        }
        
        return answer.stream()
                      .mapToInt(Integer::intValue)
                      .toArray();
    }
}