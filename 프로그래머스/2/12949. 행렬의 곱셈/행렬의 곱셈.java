import java.util.*;
class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int row1 = arr1.length;
        int col1 = arr1[0].length;
        
        for (int[] r : arr1) {
            System.out.println(Arrays.toString(r));
        }
        
        int row2 = arr2.length;
        int col2 = arr2[0].length;
        int[][] answer = new int[row1][col2];
        
        for (int[] r : arr2) {
            System.out.println(Arrays.toString(r));
        }        
        
        
        for (int r1 = 0; r1 < row1; r1++) {
            for (int c2 = 0; c2 < col2; c2++) {
                int sum = 0;
                for (int v = 0; v < col1; v++) {
                    sum += arr1[r1][v] * arr2[v][c2];
                }
                answer[r1][c2] = sum;
            }        
        }
        for (int[] r : answer) {
            System.out.println(Arrays.toString(r));
        } 
        return answer;
    }
}