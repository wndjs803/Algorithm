class Solution {
    public int countCharacters(String[] words, String chars) {
        int sum = 0;
        int wordsLength = words.length;
        
        for(int i=0; i<wordsLength; i++){
            String word = words[i];
            int length = word.length();
            int count = 0;
            String temp = chars;
            
            for(int j=0; j<length; j++){
                char c = word.charAt(j);
                if(temp.contains(Character.toString(c))){
                    temp = temp.replaceFirst(Character.toString(c), "");
                    count++;
                }else break;
            }
            if(count == length){
                sum += length;
            }
        }
        
        return sum;
    }
}