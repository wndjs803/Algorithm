import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
    
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) {
            deque.add(i);
        }

        while (deque.size() != 1) {
            deque.poll();

            if (deque.size() != 1) {
                deque.add(deque.poll());
            }
        }

        System.out.println(deque.poll());
    }
}