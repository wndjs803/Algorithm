import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static boolean[] check;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        int edge = sc.nextInt();
        graph = new ArrayList[node + 1];
        check = new boolean[node + 1];

        for (int i = 1; i <= node; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < edge; i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();

            graph[n1].add(n2);
            graph[n2].add(n1);
        }

        int count = 0;

        for (int i = 1; i <= node; i++) {
            if (!check[i]) {
                count++;
                dfs(i);        
            }
        }

        System.out.println(count);
    }

    static void dfs(int node) {
        if (check[node]) {
            return;
        }

        check[node] = true;

        for (int num : graph[node]) {
            dfs(num);
        }
    }
}