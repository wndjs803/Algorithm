class Solution {
    int left, maxLength;
    
    public void palid(String s, int start, int end){
        while(start >= 0 && end < s.length() && (s.charAt(start) == s.charAt(end))){
            start--;
            end++;
        }
        
        if(maxLength < end - start - 1){ // -1을 하는 이유는 범위는 2씩 증가했지만 substring 시에 1만큼만 크면 되기 때문
            left = start + 1;
            maxLength = end - start - 1;
        }
    }
    
    public String longestPalindrome(String s) {
        int length = s.length();
        
        if(length < 2) return s;
        
        for(int i=0; i<length; i++){
            palid(s, i, i+1);
            palid(s, i, i+2);
        }
        
        return s.substring(left, left + maxLength);
    }
}