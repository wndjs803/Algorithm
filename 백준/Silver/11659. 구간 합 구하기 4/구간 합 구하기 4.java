import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int[] sumArr = new int[N];
        sumArr[0] = arr[0];

        for (int i = 1; i < N; i++) {
            sumArr[i] = sumArr[i - 1] + arr[i];
        }

        for (int i = 0; i < M; i++) {
            int start = sc.nextInt() - 1;
            int end = sc.nextInt() - 1;

            if (start > 0) {
                System.out.println(sumArr[end] - sumArr[start -1]);
            }
            else System.out.println(sumArr[end]);
        }
    }
}
