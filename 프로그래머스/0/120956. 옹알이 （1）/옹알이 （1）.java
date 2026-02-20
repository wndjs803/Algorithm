class Solution {
    public int solution(String[] babbling) {
        String[] keyword = {"aya", "ye", "woo", "ma"};
        int answer = 0;
        
        for (String str : babbling) {
            int i = 0;
            
            while (i < 4) {
                if (str.startsWith(keyword[i])) {
                    if (str.equals(keyword[i])) {
                        answer++;
                        break;
                    }
                    else {
                        str = str.substring(keyword[i].length(), str.length());
                        i = 0;
                    }
                }
                else i++;
            }
        }
        
        return answer;
    }
}