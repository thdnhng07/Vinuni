
// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 01 – Week 01 – Getting started with Java
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 4-------------------------------
//                             Check Permutations
//-----------------------------------------------------------------------------
package Lab2;

import java.util.Scanner;

public class Lab02_P4 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt();
        
        if (T < 1 || T > 100) {
            System.out.println("Number of test cases must be between 1 and 100.");
            scanner.close();
            return;
        }
        
        for (int t = 1; t <= T; t++) {

            int n = scanner.nextInt();
            
            if (n < 1 || n > 100000) {
                System.out.println("n must be between 1 and 100000.");
                scanner.close();
                return;
            }
            
            int[] arr = new int[n];
            boolean[] appears = new boolean[n + 1];
            
            for (int i = 1; i <= n; i++) {
                appears[i] = false;
            }
            
            boolean is_permutation = true;
            
            for (int i = 0; i < n; i++) {
                arr[i] = scanner.nextInt();

                if (arr[i] < 1 || arr[i] > n) {
                    is_permutation = false;
                } else {

                    if (appears[arr[i]]) {

                        is_permutation = false;
                    } else {
                        appears[arr[i]] = true;
                    }
                }
            }
            

            if (is_permutation) {
                for (int i = 1; i <= n; i++) {
                    if (!appears[i]) {
                        is_permutation = false;
                        break;
                    }
                }
            }
            

            System.out.println(is_permutation ? 1 : 0);
        }
        
        scanner.close();
    }
}
