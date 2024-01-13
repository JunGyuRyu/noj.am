import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        Map<Long, Integer> map = new HashMap<>();

        for (int i = 0; i < N; i++) {
            long l = Long.parseLong(bf.readLine());
            map.put(l, map.getOrDefault(l, 0) + 1);
        }
        Set<Long> unique = map.keySet();
        long[][] arr = new long[unique.size()][2];
        Iterator<Long> keys = unique.iterator();
        Iterator<Integer> values = map.values().iterator();

        for (int i = 0; i < map.keySet().size(); i++) {
            arr[i][0] = keys.next();
            arr[i][1] = values.next();
        }
        Arrays.sort(arr, (a, b) -> {
            if (a[1] == b[1]) {
                return Long.compare(a[0], b[0]);
            }
            return Long.compare(b[1], a[1]);
        });
        System.out.println(arr[0][0]);
    }
}