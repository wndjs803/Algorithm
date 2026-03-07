import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken()) - 1;

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        quickSelect(0, n - 1, arr, k);

        System.out.println(arr[k]);
    }

    static void quickSelect(int start, int end, int[] arr, int k) {

        if (start >= end) return;

        int left = start;
        int right = end;

        int pivotIndex = (start + end) / 2;
        int pivotValue = arr[pivotIndex];

        while (left <= right) {

            while (arr[left] < pivotValue) left++;
            while (arr[right] > pivotValue) right--;

            if (left <= right) {
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;

                left++;
                right--;
            }
        }

        if (k <= right) {
            quickSelect(start, right, arr, k);
        } else if (k >= left) {
            quickSelect(left, end, arr, k);
        }
    }
}