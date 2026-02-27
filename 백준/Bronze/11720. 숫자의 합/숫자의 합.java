import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String str = sc.next();
        int sum = 0;

        for(char c : str.toCharArray()) {
            sum += c - '0';
        }

        System.out.println(sum);
    }
}
