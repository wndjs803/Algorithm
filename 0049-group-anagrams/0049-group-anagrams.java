class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> answers = new HashMap<>();
        for(String s : strs){
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            
            String key = new String(charArray);
            
            if(!answers.containsKey(key)){
                answers.put(key, new ArrayList<>());
            }
            answers.get(key).add(s);
        }
        
        return new ArrayList<>(answers.values());
    }
}