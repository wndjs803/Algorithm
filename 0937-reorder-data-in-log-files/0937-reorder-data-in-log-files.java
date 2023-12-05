class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letters = new ArrayList<>();
        List<String> digits = new ArrayList<>();
        
        for(String s : logs){
            if(Character.isLetter(s.split(" ")[1].charAt(0))){
                letters.add(s);
            }else digits.add(s);
        }
        
        letters.sort((s1, s2) ->{
            String[] c1 = s1.split(" ", 2);
            String[] c2 = s2.split(" ", 2);
            
            int compare = c1[1].compareTo(c2[1]);
            
            if(compare == 0){
                return c1[0].compareTo(c2[0]);
            }else return compare;
        });
            
        letters.addAll(digits);
        
        return letters.toArray(new String[0]);
    }
}