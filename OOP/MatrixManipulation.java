// import java.util.Scanner;
// public class Rectangle {
// 	int length;
// 	int width;
// 	public static void main(String[] args) {
// 		// TODO Auto-generated method stub
// 		Scanner input = new Scanner(System.in);
// 		int L = input.nextInt();
// 		int W = input.nextInt();
// 		Rectangle rectangle = new Rectangle(L,W);
// 		System.out.print(rectangle.computeArea() + " " + rectangle.computePerimeter());
		
// 	}
// 		public Rectangle(int l, int w) {
// 			this.length = l;
// 			this.width = w;
// 		}
// //		Method to compute area
// 		public int computeArea() {
// 			return width * length;
// 		}
// //		Method to compute perimeter
// 		public int computePerimeter() {
// 			return (length + width) * 2;
// 		}
// }

import java.util.Scanner;
import java.util.ArrayList;

public class MatrixManipulation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<String> lines = new ArrayList<>();

        String line;
        while (true) {
            line = input.nextLine();
            if (line.equals("#")) break;
            lines.add(line);
        }

        String[] dims = lines.get(0).split(" ");
        int m = Integer.parseInt(dims[0]);
        int n = Integer.parseInt(dims[1]);

        int[][] matrix = new int[m][n];
        for (int i = 0; i < m; i++) {
            String[] rowValues = lines.get(i + 1).split(" ");
            for (int j = 0; j < n; j++) {
                matrix[i][j] = Integer.parseInt(rowValues[j]);
            }
        }

        for (int i = m + 1; i < lines.size(); i++) {
            String[] command = lines.get(i).split(" ");

            if (command[0].equals("sum")) {
                System.out.println(sum(matrix, m, n));
            } else if (command[0].equals("subsum")) {
                int a = Integer.parseInt(command[1]) - 1;
                int b = Integer.parseInt(command[2]) - 1;
                int c = Integer.parseInt(command[3]) - 1;
                int d = Integer.parseInt(command[4]) - 1;
                System.out.println(subsum(matrix, a, b, c, d));
            } else if (command[0].equals("update")) {
                int r = Integer.parseInt(command[1]) - 1;
                int c = Integer.parseInt(command[2]) - 1;
                int v = Integer.parseInt(command[3]);
                matrix[r][c] = v;
            }
        }

        input.close();
    }

    public static int sum(int[][] matrix, int m, int n) {
        int total = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                total += matrix[i][j];
            }
        }
        return total;
    }

    public static int subsum(int[][] matrix, int a, int b, int c, int d) {
        int total = 0;
        for (int i = a; i <= c; i++) {
            for (int j = b; j <= d; j++) {
                total += matrix[i][j];
            }
        }
        return total;
    }
}