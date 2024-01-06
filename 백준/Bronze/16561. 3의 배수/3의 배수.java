import java.lang.*;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int cnt = 0;
        for (int i = 3; i <= n - 6; i += 3) {
            for (int j = 3; j <= n - 3 - i; j += 3) {
                cnt++;
            }
        }
        System.out.println(cnt);
        scanner.close();
    }
}