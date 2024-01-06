import java.util.Scanner;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        N = sc.nextInt();
        sc.close();
        
        arr = IntStream.range(1, N + 1).toArray();
        permutate(new int[N], new boolean[N], 0);
    }

    static int N;
    static int[] arr;

    public static void permutate(int[] tmp, boolean[] visited, int depth) {
        if (depth == N) {
            StringBuilder sb = new StringBuilder();
            for (int el : tmp) {
                sb.append(el);
                sb.append(" ");
            }
            System.out.println(sb.toString().trim());
            return;
        }
        for (int i = 0; i < N; i++) {
            if (visited[i]) {
                continue;
            }
            tmp[depth] = arr[i];
            visited[i] = true;
            permutate(tmp, visited, depth + 1);
            visited[i] = false;
        }
    }
}