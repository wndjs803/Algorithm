import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        float[] scores = new float[size];
        float max = -1;

        for (int i = 0; i < size; i++) {
            scores[i] = sc.nextFloat();

            if (max <= scores[i]) {
                max = scores[i];
            }
        }

        float sum = 0;
        for (float score : scores) {
            sum += (score / max) * 100;
        }

        System.out.println(sum / size);

    }
}
