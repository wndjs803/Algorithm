import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] answer = new int[n + 1];
        Deque<Integer> deque = new ArrayDeque<>();

        int i = 1;
        while (i <= n) {
            int start = i - l + 1;
            
            if (start <= 1) {
                if (deque.isEmpty()) {
                    deque.add(i);
                }
                else {
                    while (true) {
                        if (!deque.isEmpty() && arr[deque.peekLast()] >= arr[i]) {
                            deque.pollLast();
                        }
                        else {
                            deque.add(i);
                            break;
                        }
                    }
                }
            }
            else {
                if (deque.peek() < start) {
                    deque.poll();
                }
                while (true) {
                    if (!deque.isEmpty() && arr[deque.peekLast()] >= arr[i]) {
                        deque.pollLast();
                    }
                    else {
                        deque.add(i);
                        break;
                    }
                }
            }

            answer[i] = arr[deque.peek()];

            i++;
        }

        StringBuilder sb = new StringBuilder();

        for (int j = 1; j <= n; j++) {
            sb.append(answer[j]).append(" ");
        }

        System.out.println(sb.toString());
    }

}