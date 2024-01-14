class Solution {
    public boolean closeStrings(String word1, String word2) {
        int count1 = 0;
        int count2 = 0;
        
        int length1 = word1.length();
        int length2 = word2.length();
        if(length1 != length2) return false;
        
        Map<String, Integer> s1 = new HashMap<>();
        Map<String, Integer> s2 = new HashMap<>();
        
        for(int i=0; i<length1; i++){
            String key1 = Character.toString(word1.charAt(i));
            String key2 = Character.toString(word2.charAt(i));
            
            s1.put(key1, s1.getOrDefault(key1, 0) + 1);
            s2.put(key2, s2.getOrDefault(key2, 0) + 1);
        }
        
        Set<String> keySet1 = s1.keySet();
        Set<String> keySet2 = s2.keySet();
        
        if(!keySet1.equals(keySet2)) return false;
        
        List<Integer> valuesList1 = new ArrayList<>(s1.values());
        List<Integer> valuesList2 = new ArrayList<>(s2.values());
        
        Collections.sort(valuesList1);
        Collections.sort(valuesList2);
        
        if(valuesList1.equals(valuesList2)) return true;
        else return false;
    }
}