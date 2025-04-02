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

public class Lab02_P03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();

        int[][] A = new int[n][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                A[i][j] = scanner.nextInt();
            }
        }


        int k2 = scanner.nextInt();
        int m = scanner.nextInt();

        int[][] B = new int[k][m];
        for (int i = 0; i < k; i++) {
            for (int j = 0; j < m; j++) {
                B[i][j] = scanner.nextInt();
            }
        }

        int[][] C = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                C[i][j] = 0;
                for (int t = 0; t < k; t++) {
                    C[i][j] += A[i][t] * B[t][j];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(C[i][j] + " ");
            }
            System.out.println();
        }

        scanner.close();
    }
}
