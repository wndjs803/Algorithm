class Solution {
    public String solution(String rny_string) {
        String[] rnyArr = rny_string.split("");
        
        for (int i = 0; i < rnyArr.length; i++) {
            if (rnyArr[i].equals("m")) rnyArr[i] = "rn";
        }
        
        return String.join("", rnyArr);
    }
}