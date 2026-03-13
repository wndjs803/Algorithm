import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    static int n;
    static int count = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        backtracking(0);
        System.out.println(count);
    }

    static void backtracking(int row) {
        if (row == n) {
            count++;
            return;
        }
        
        for (int i = 0; i < n; i++) {
            arr[row] = i;
            
            if (confirm(row)) {
                backtracking(row + 1);
            }
        }
    }

    static boolean confirm(int row) {
        // 같은 열, 대각 선 확인
        for (int i = 0; i < row; i++) {
            if (arr[row] == arr[i]) {
                return false;
            }

            if (Math.abs(row - i) == Math.abs(arr[row] - arr[i])) {
                return false;
            }
        }
 
        return true;
    }
}