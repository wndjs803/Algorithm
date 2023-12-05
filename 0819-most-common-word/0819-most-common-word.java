import java.util.HashMap;
import java.util.Map;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        String[] words = paragraph.replaceAll("\\W+", " ").toLowerCase().split(" ");
        HashMap<String, Integer> count = new HashMap<>();
        int maxCount = -1;
        String result = paragraph;
        
        for(String word : words){
            if(count.containsKey(word)){
                int curCount = count.get(word);
                count.put(word, curCount+1);
            }else{
                count.put(word, 1);
            }
        }
        
        if(banned.length != 0){
            for(String bannedWord : banned){
                count.remove(bannedWord);
            }
        }
        
        for(Map.Entry<String, Integer> entry : count.entrySet()){
            int totalCount = entry.getValue();
            if(maxCount <= totalCount){
                maxCount = totalCount;
                result = entry.getKey();
            }
        }
        
        return result;
    }
}