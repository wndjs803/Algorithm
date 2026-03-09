import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    static int[] temp;
    static long result = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[n];
        temp = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        mergeSort(0, n - 1);

        System.out.println(result);
    }

    static void mergeSort(int left, int right) {
        if (left >= right) {
            return;
        }

        int mid = (left + right) / 2;

        mergeSort(left, mid);
        mergeSort(mid + 1, right);

        int i = left;
        int l = left;
        int r = mid + 1;

        while (l <= mid && r <= right) {
            if (arr[l] <= arr[r]) {
                temp[i] = arr[l];
                i++;
                l++;
            }
            else {
                temp[i] = arr[r];
                result += r - i;
                i++;
                r++;
            }
        }

        while (l <= mid) {
            temp[i] = arr[l];
            i++;
            l++;
        }
        while (r <= right) {
            temp[i] = arr[r];
            i++;
            r++;
        }

        for (int j = left; j <= right; j++) {
            arr[j] = temp[j];
        }
    }
}