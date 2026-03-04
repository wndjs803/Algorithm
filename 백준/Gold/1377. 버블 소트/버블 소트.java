import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Data[] arr = new Data[n];

        for (int i = 0; i < n; i++) {
            arr[i] = new Data(i, Integer.parseInt(br.readLine()));
        }

        Arrays.sort(arr);

        int max = -1;
        for (int i = 0; i < n; i++) {
            if (arr[i].index - i >= max) {
                max = arr[i].index - i;
            }
        }

        System.out.println(max + 1);
    }

    
    static class Data implements Comparable<Data> {
        int index;
        int value;

        public Data(int index, int value) {
            this.index = index;
            this.value = value;
        }

        @Override
        public int compareTo(Data d) {
            return this.value - d.value;
        }
    }
}
