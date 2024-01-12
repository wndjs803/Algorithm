class Solution {
    public boolean halvesAreAlike(String s) {
        int left = 0;
        int right = 0;
        int length = s.length();
        
        for(int i=0; i<length; i++){
            char c = Character.toLowerCase(s.charAt(i));
            if((c=='a') || (c=='e') || (c=='i') || (c=='o') || (c=='u')){
                if(i < length/2){
                    left += 1;
                }else right += 1;
            }
        }
        return left == right;
    }
}