import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        int[] scores = new int[size];
        int max = -1;
        int sum = 0;

        for (int i = 0; i < size; i++) {
            scores[i] = sc.nextInt();
            sum += scores[i];

            if (max <= scores[i]) {
                max = scores[i];
            }
        }

        System.out.println(sum * 100.0 / max / size);
    }
}
