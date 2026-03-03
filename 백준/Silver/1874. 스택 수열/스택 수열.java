import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        Deque<Integer> deque = new ArrayDeque<>();
        int i = 1;
        boolean possible = true;

        for (int num : arr) {

            while (i <= n && (deque.isEmpty() || deque.peekLast() < num)) {
                deque.addLast(i++);
                sb.append("+\n");
            }

            if (!deque.isEmpty() && deque.peekLast() == num) {
                deque.pollLast();
                sb.append("-\n");
            } else {
                possible = false;
                break;
            }
        }

        if (!possible) {
            System.out.println("NO");
        } else {
            System.out.print(sb);
        }
    }
}