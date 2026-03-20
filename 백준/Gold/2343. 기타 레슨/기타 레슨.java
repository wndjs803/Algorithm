import java.util.*;

public class Main {
    static int[] arr;
    static int m;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        m = sc.nextInt();

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int start = Arrays.stream(arr).max().getAsInt();
        int end = Arrays.stream(arr).sum();

        while (start <= end) {
            int midValue = (start + end) / 2;

            if (isSuccess(midValue)) {
                end = midValue - 1;
            }
            else {
                start = midValue + 1;
            }
        }

        System.out.println(start);

    }

    static boolean isSuccess(int midValue) {
        int count = 0;
        int sum = 0;
        for (int num : arr) {
            if (sum + num > midValue) {
                count++;
                sum = 0;
            }
            sum += num;
        }

        if (sum != 0) {
            count++;
        }

        if (count <= m) {
            return true;
        }
        return false;
    }
}
