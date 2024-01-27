import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] l = new int[10];
        l[0] = 1;
        l[1] = 2;
        l[2] = 4;
        for (int i = 3; i < 10; i++) {
            l[i] = l[i-1] + l[i-2] + l[i-3];
        }

        for (int i = 0; i < T; i++) {
            int n = sc.nextInt();
            System.out.println(l[n - 1]);
        }
        sc.close();
    }
}