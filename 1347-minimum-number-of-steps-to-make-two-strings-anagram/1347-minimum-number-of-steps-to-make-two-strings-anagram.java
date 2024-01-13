class Solution {
    public int minSteps(String s, String t) {
        int result = 0;
        
        Map<String, Integer> hashMap = new HashMap<>();
        
        for(int i=0; i<t.length(); i++){
            String key = Character.toString(t.charAt(i));
            hashMap.put(key, hashMap.getOrDefault(key, 0) + 1);
        }
        
        for(int i=0; i<s.length(); i++){
            String arg = Character.toString(s.charAt(i));
            if(hashMap.containsKey(arg)){
                int value = hashMap.get(arg);
                if(value > 0){
                    hashMap.put(arg, value-1);
                }
                else result += 1;
            }else result += 1;
        }
        
        return result;
    }
}