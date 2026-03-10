import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static boolean[] check;
    static int result = 0;
    static int depth;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int node = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());

        check = new boolean[node];
        graph = new ArrayList[node];

        for (int i = 0; i < node; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.parseInt(st.nextToken());
            int n2 = Integer.parseInt(st.nextToken());

            graph[n1].add(n2);
            graph[n2].add(n1);
        }

        for (int i = 0; i < node; i++) {
            depth = 0;
            dfs(i, depth);
            
            if (result == 1) {
                break;
            }
        }

        if (result != 1) System.out.println(0);
    }

    static void dfs(int num, int depth) {
        if (result == 1) return;

        if (depth == 4) {
            result = 1;
            System.out.println(result);
            return;
        }

        if (check[num]) return;

        check[num] = true;

        for (int n : graph[num]) {
            if (!check[n]) {
                dfs(n, depth + 1);
            }
        }
        
        check[num] = false;
    }
}