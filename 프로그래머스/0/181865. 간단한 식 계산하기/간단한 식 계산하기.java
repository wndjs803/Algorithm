class Solution {
    public int solution(String binomial) {
        String[] binomialArr = binomial.split(" ");
        int a = Integer.parseInt(binomialArr[0]);
        int b = Integer.parseInt(binomialArr[2]);
        String op = binomialArr[1];
        int answer = 0;
        
        switch (op) {
            case "+": answer = a + b;
                      break;
            case "-": answer = a - b;
                      break;
            case "*": answer = a * b;
                      break;
        }
        
        return answer;
    }
}