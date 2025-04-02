// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 03 – Week 04
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                             Matrix Manipulation
//-----------------------------------------------------------------------------
package Lab3;
import java.util.Scanner;
import java.util.ArrayList;

class Matrix {
    private int rows, cols;
    private int[][] matrix;

    public Matrix(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        this.matrix = new int[rows][cols];
    }

    public void setMatrix(ArrayList<ArrayList<Integer>> data) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                matrix[i][j] = data.get(i).get(j);
            }
        }
    }

    public int sum() {
        int total = 0;
        for (int[] row : matrix) {
            for (int element : row) {
                total += element;
            }
        }
        return total;
    }

    public int subsum(int a, int b, int c, int d) {
        int total = 0;
        for (int i = a - 1; i < b; i++) {
            for (int j = c - 1; j < d; j++) {
                total += matrix[i][j];
            }
        }
        return total;
    }

    public void update(int r, int c, int v) {
        matrix[r - 1][c - 1] = v;
    }
}

public class MatrixManipulation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();

        ArrayList<ArrayList<Integer>> matrixData = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            ArrayList<Integer> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                row.add(scanner.nextInt());
            }
            matrixData.add(row);
        }

        Matrix mat = new Matrix(m, n);
        mat.setMatrix(matrixData);

        ArrayList<String> operations = new ArrayList<>();
        scanner.nextLine();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();
            if (line.equals("#")) break;
            operations.add(line);
        }

        for (String operation : operations) {
            String[] parts = operation.split(" ");
            switch (parts[0]) {
                case "sum":
                    System.out.println(mat.sum());
                    break;
                case "subsum":
                    int a = Integer.parseInt(parts[1]);
                    int b = Integer.parseInt(parts[2]);
                    int c = Integer.parseInt(parts[3]);
                    int d = Integer.parseInt(parts[4]);
                    System.out.println(mat.subsum(a, b, c, d));
                    break;
                case "update":
                    int r = Integer.parseInt(parts[1]);
                    int t = Integer.parseInt(parts[2]);
                    int v = Integer.parseInt(parts[3]);
                    mat.update(r, t, v);
                    break;
            }
        }

        scanner.close();
    }
}
