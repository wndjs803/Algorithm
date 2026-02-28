import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        
        int count = 0;

        for (int i = 0; i < n; i++) {
            int num = arr[i];
            int start = 0;
            int end = n - 1;

            while (start < end) {
                int sum = arr[start] + arr[end];

                if (sum < num) {
                    start++;
                }
                else if (sum > num) {
                    end--;
                }
                else if (sum == num) {
                    if (start != i && end != i) {
                        count++;
                        break;
                    }
                    else if (start == i) {
                        start++;
                    }
                    else if (end == i) {
                        end--;
                    }
                }
            }
        }

        System.out.println(count);
    }
}