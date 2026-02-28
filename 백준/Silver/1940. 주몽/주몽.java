import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int start = 0;
        int end = n - 1;
        int count = 0;

        while (end != start) {
            int sum = arr[start] + arr[end];

            if (sum < m) {
                start++;
            }

            else if (sum > m) {
                end--;
            }

            else if (sum == m) {
                count++;
                start++;
            }
        }

        System.out.println(count);
    }
}