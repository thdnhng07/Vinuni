// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 01 – Week 01 – Getting started with Java
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                                   Primes
//-----------------------------------------------------------------------------
package Lab2;

import java.util.Scanner;

public class Lab2_p2 {

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int [] f = new int [n+1];

        for (int i = 0; i <= n; i++) {
            f[i] = 0;
        }
        

        for (int i = 2; i <= n; i++) {
            if (f[i] == 0) {
                System.out.print(i + " ");
                
                int j = i;
                while (j <= n) {
                    f[j] = 1;
                    j = j + i;
                }
            }
        }
        System.out.println();
        scanner.close();
    }
}
