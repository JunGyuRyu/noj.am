import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(
                new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());

        graph = new boolean[N + 1][N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = true;
            graph[b][a] = true;
        }
        visit = new boolean[N + 1];
        sb = new StringBuilder();
        dfs2(V);
        System.out.println(sb);
        visit = new boolean[N + 1];
        sb = new StringBuilder();
        bfs(V);
        System.out.println(sb);
    }

    static boolean[] visit;
    static boolean[][] graph;
    static StringBuilder sb;

    static void dfs(int node) {
        visit[node] = true;
        sb.append(node);
        sb.append(' ');
        for (int i = 1; i < graph[node].length; i++) {
            if (graph[node][i] && !visit[i]) {
                dfs(i);
            }
        }
    }

    static void dfs2(int node) {
        Stack<Integer> stack = new Stack<>();
        stack.push(node);
        while (!stack.isEmpty()) {
            int nextNode = stack.pop();
            if (visit[nextNode]) {
                continue;
            } else {
                visit[nextNode] = true;
            }
            sb.append(nextNode);
            sb.append(' ');
            for (int i = graph[nextNode].length - 1; i >= 1; i--) {
                if (!graph[nextNode][i]) {
                    continue;
                }
                stack.push(i);
            }
        }
    }

    static void bfs(int node) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(node);
        while (!queue.isEmpty()) {
            int nextNode = queue.poll();
            if (visit[nextNode]) {
                continue;
            } else {
                visit[nextNode] = true;
            }
            sb.append(nextNode);
            sb.append(' ');
            for (int i = 1; i <= graph[nextNode].length - 1; i++) {
                if (!graph[nextNode][i]) {
                    continue;
                }
                queue.add(i);
            }
        }
    }
}