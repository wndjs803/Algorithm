import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int N = Integer.parseInt(stringTokenizer.nextToken());
        int M = Integer.parseInt(stringTokenizer.nextToken());
        long[] arr = new long[N];

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Long.parseLong(stringTokenizer.nextToken());
        }

        long[] sumArr = new long[N];
        sumArr[0] = arr[0];
        for (int i = 1; i < N; i++) {
            sumArr[i] = sumArr[i - 1] + arr[i];
        }

        long answer = 0;
        long[] remainders = new long[M];
        for (int i = 0; i < N; i++) {
            int remainder = (int) (sumArr[i] % M);
            remainders[remainder]++;
            if (remainder == 0) answer++;
        }

        for (long count : remainders) {
            if (count > 1) {
                answer += count * (count - 1) / 2;
            }
        }

        System.out.println(answer);
    }
}
