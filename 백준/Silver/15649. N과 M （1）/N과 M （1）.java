import java.io.*;
import java.util.*;

public class Main {
    static boolean[] check;
    static int[] arr;
    static int n;
    static int m;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        check = new boolean[n + 1];
        arr = new int[n];

        backtracking(0);
    }

    static void backtracking(int length) {
        if (length == m) {
            for (int i = 0; i < m; i++) {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (!check[i]) {
                check[i] = true;
                arr[length] = i;
                backtracking(length + 1);
                check[i] = false;
            }
        }
    }
}