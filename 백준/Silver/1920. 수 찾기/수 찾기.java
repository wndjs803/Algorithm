import java.util.*;

public class Main {
    static int[] arr;

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int m = sc.nextInt();

        Arrays.sort(arr);

        for (int i = 0; i < m; i++) {
            System.out.println(binarySearch(sc.nextInt()));
        }
    }

    static int binarySearch(int num) {
        int start = 0;
        int end = arr.length - 1;
        int index = (start + end) / 2;

        while (start <= end) {
            index = (start + end) / 2;
            if (arr[index] > num) {
                end = index - 1;
            }
            else if (arr[index] < num) {
                start = index + 1;
            }
            else if (arr[index] == num) {
                return 1;
            }
        }
        return 0;
    }
}