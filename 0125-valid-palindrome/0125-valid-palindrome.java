class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder alpha = new StringBuilder();
        boolean result = true;
        
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c) || Character.isDigit(c)) {
                alpha.append(c);
            }
        }
        
        int length = alpha.length();
        for(int i=0; i<length/2; i++){
            if(Character.toUpperCase(alpha.charAt(i)) != Character.toUpperCase(alpha.charAt(length-i-1))){
                result = false;
                break;
            }
        }
        
        return result;
    }
}