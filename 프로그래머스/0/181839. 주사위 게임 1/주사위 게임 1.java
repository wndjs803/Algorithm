class Solution {
    public int solution(int a, int b) {
        int sum = (a % 2) + (b % 2);
        
        if (sum == 2) {
            return a*a + b*b;
        }
        if (sum == 1) {
            return 2 * (a + b);
        }
        return Math.abs(a - b);
    }
}