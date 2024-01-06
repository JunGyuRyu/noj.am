import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int[][] arr = new int[3][3];
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				int el = scanner.nextInt();
				arr[i][j] = el;
			}
			// System.out.println();
		}
		int[][][] squares = getSquares();
		int minCost = Integer.MAX_VALUE;
        
		for (int i = 0; i < 8; i++) {
			int[][] s = squares[i];
			int cost = 0;
			for (int j = 0; j < 3; j++) {
				for (int k = 0; k < 3; k++) {
					cost += Math.abs(s[j][k] - arr[j][k]);
				}
			}			
			minCost = minCost > cost ? cost : minCost;
		}
		System.out.println(minCost);
		scanner.close();
	}

	public static int[][][] getSquares() {
		int[][] ms = {
				{8, 3, 4},
				{1, 5, 9},
				{6, 7, 2}
			};
		int[][][] msArr = new int[8][3][3];
		for (int i = 0; i < 8; i++) {
			if (i == 0) {				
				msArr[i] = ms.clone();
			} else {				
				int[][] rt = new int[3][3];
				if (i < 4) {				
					for (int j = 0; j < 3; j++) {
						for (int k = 0; k < 3; k++) {
							rt[k][2-j] = msArr[i-1][j][k];
						}
					}
				} else {
					for (int j = 0; j < 3; j++) {
						for (int k = 0; k < 3; k++) {
							rt[j][2-k] = msArr[i-4][j][k];
						}
					}
				}
				msArr[i] = rt.clone();
			}
		}
		return msArr;
	}
}