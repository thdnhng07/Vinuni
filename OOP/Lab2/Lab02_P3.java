// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 01 – Week 01 – Getting started with Java
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 3-------------------------------
//                            Matrix  multiplication
//-----------------------------------------------------------------------------
package Lab2;

import java.util.Scanner;

public class Lab02_P3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt(), k = scanner.nextInt();

        if (n < 1 || n > 100 || k < 1 || k > 100) {
            System.out.println("Invalid dimensions for matrix A. n and k must be between 1 and 100.");
            scanner.close();
            return;
        }

        int[][] A = new int[n][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                A[i][j] = scanner.nextInt();

                if (A[i][j] < 1 || A[i][j] > 50) {
                    System.out.println("Invalid element in matrix A. Elements must be between 1 and 50.");
                    scanner.close();
                    return;
                }
            }
        }

        int m = scanner.nextInt();

        if (m < 1 || m > 100) {
            System.out.println("Invalid dimensions for matrix B. m must be between 1 and 100.");
            scanner.close();
            return;
        }

        int[][] B = new int[k][m];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < m; j++) {
                B[i][j] = scanner.nextInt();

                if (B[i][j] < 1 || B[i][j] > 50) {
                    System.out.println("Invalid element in matrix B. Elements must be between 1 and 50.");
                    scanner.close();
                    return;
                }
            }
        }

        int[][] C = matrixMultiply(A, B, n, k, m);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(C[i][j]);
                if (j < m - 1) {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        scanner.close();
    }

    public static int[][] matrixMultiply(int[][] A, int[][] B, int n, int k, int m) {
        int[][] C = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                C[i][j] = 0;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int t = 0; t < k; t++) {
                    C[i][j] = C[i][j] + (A[i][t] * B[t][j]);
                }
            }
        }

        return C;
    }
}
