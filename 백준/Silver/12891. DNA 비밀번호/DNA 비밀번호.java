import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int p = sc.nextInt();
        char[] passowrd = sc.next().toCharArray();
        int aCount = sc.nextInt();
        int cCount = sc.nextInt();
        int gCount = sc.nextInt();
        int tCount = sc.nextInt();

        int start = 0;
        int end = p - 1;
        int answer = 0;

        Map<Character, Integer> counter = new HashMap<>();
        for (int i = start; i <= end; i++) {
            counter.put(passowrd[i], counter.getOrDefault(passowrd[i], 0) + 1);
        }

        if (counter.getOrDefault('A', 0) >= aCount &&
                counter.getOrDefault('C', 0) >= cCount && 
                counter.getOrDefault('G', 0) >= gCount && 
                counter.getOrDefault('T', 0) >= tCount) {
                answer++;
        }

        start++;
        end++;

        while (end < s) {
            counter.put(passowrd[start - 1], counter.get(passowrd[start - 1]) - 1);
            counter.put(passowrd[end], counter.getOrDefault(passowrd[end], 0) + 1);

            if (counter.getOrDefault('A', 0) >= aCount &&
                counter.getOrDefault('C', 0) >= cCount && 
                counter.getOrDefault('G', 0) >= gCount && 
                counter.getOrDefault('T', 0) >= tCount) {
                answer++;
            }

            start++;
            end++;
        }

        System.out.println(answer);
    }
}