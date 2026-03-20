import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int start = 1;
        int end = k;

        while (start <= end) {
            int midValue = (start + end) / 2;
            int sum = 0;

            for (int i = 1; i <= n; i++) {
                sum += (int)Math.min(midValue / i, n);
            }

            if (sum < k) {
                start = midValue + 1;
            }
            else {
                end = midValue - 1;
            }
        }

        System.out.println(start);
    }
}
