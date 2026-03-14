import java.util.*;

public class Main {
    static List<Integer>[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int node = sc.nextInt();
        int edge = sc.nextInt();
        int start = sc.nextInt();

        graph = new ArrayList[node + 1];

        for (int i = 1; i <= node; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < edge; i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();

            graph[n1].add(n2);
            graph[n2].add(n1);
        }

        for (int i = 1; i <= node; i++) {
            Collections.sort(graph[i]);
        }

        visited = new boolean[node + 1];
        dfs(start);

        System.out.println();

        visited = new boolean[node + 1];
        bfs(start);
    }

    static void dfs(int node) {
        if (visited[node]) {
            return;
        }

        System.out.print(node + " ");
        visited[node] = true;

        for (int i = 0; i < graph[node].size(); i++) {
            int n = graph[node].get(i);

            if (!visited[n]) {
                dfs(n);
            }
        }
    }

    static void bfs(int node) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(node);

        while (!queue.isEmpty()) {
            int n = queue.poll();

            if (visited[n]) {
                continue;                
            }

            visited[n] = true;
            System.out.print(n + " ");

            for (Integer integer : graph[n]) {
                queue.add(integer);
            }
        }
    }
}