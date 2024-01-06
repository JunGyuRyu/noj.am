import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        boolean remain[] = new boolean[42];
		Scanner scanner = new Scanner(System.in);
		int cnt = 0;
		for (int i = 0; i < 10; i++) {
			int mod = scanner.nextInt() % 42;
			if (remain[mod]) {
				continue;
			}
			cnt++;
			remain[mod] = true;
		}
		System.out.println(cnt);
		scanner.close();
    }
}

