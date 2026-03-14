import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] arr;
    // 상 하 좌 우
    static int[] moveX = {-1, 1, 0, 0};
    static int[] moveY = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        arr = new int[n][m];

        for (int i = 0; i < n; i++) {
            char[] row = sc.next().toCharArray();
            for (int j = 0; j < m; j++) {
                arr[i][j] = row[j] - '0';
            }
        }

        bfs(new Coordinate(0, 0, 1));
    }

    static void bfs(Coordinate coordinate) {
        Queue<Coordinate> queue = new ArrayDeque<>();
        queue.add(coordinate);
        Coordinate current = null;

        while (!queue.isEmpty()) {
            current = queue.poll();
            int curX = current.getX();
            int curY = current.getY();

            if (curX == n -1 && curY == m - 1) {
                break;
            }

            if (arr[curX][curY] != 1) {
                continue;
            }

            arr[curX][curY] = 0;

            for (int i = 0; i < 4; i++) {
                int dx = curX + moveX[i];
                int dy = curY + moveY[i];

                if (dx >= 0 && dx < n && dy >= 0 && dy < m) {
                    if (arr[dx][dy] == 1) {
                        queue.add(new Coordinate(dx, dy, current.getCount() + 1));
                    }
                }
            }

        }

        System.out.println(current.getCount());
    }

    static class Coordinate {
        int x;
        int y;
        int count;

        public Coordinate(int x, int y, int count) {
            this.x = x;
            this.y = y;
            this.count = count;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getCount() {
            return count;
        }
    }
}