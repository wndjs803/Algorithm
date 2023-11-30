class Solution {
    public int maxScore(String s) {
        String right;
        String left;
        int last = s.length()-1;
        int length = s.length();
        int rightScore, leftScore, total;
        int result = 0;

        for(int i=1; i<=last; i++){
            rightScore = 0;
            leftScore = 0;

            left = s.substring(0, i);
            for(String l : left.split("")){
                if(l.equals("0")){
                    leftScore += 1;
                }
            }

            right = s.substring(i, length);
            for(String r : right.split("")){
                if(r.equals("1")){
                    rightScore += 1;
                }
            }
            total = leftScore + rightScore;
            if(result <= total){
                result = total;
            }
        }

        return result;
    }
}