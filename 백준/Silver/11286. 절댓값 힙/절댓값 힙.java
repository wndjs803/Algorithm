import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
    
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> {
            if (Math.abs(a) == Math.abs(b)) {
                return a - b;
            }
            return Math.abs(a) - Math.abs(b);
        });

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();

            if (num != 0) {
                pq.add(num);
            }
            else {
                if (pq.isEmpty()) {
                    System.out.println(0);
                }
                else System.out.println(pq.poll());
            }
        }
    }
}