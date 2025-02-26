//VinUniversity, Spring 2025

//COMP1020 Object-Oriented Programming and Data Structures

//Lab 01 – Week 01 – Getting started with Java

//by Dat Thanh – V202401381

//Date: Feb 21, 2025

//Disclaimer: I certify that this assignment is my own work and that I have not copied in part

//or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 4-------------------------------

//                             Solving quadratic functions

//-----------------------------------------------------------------------------
package Lab1;

import java.util.Scanner;

public class Quadratic {
    public static void main(String[] args){

        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();

        scanner.close();

        double delta = b * b - 4 * a * c;


        if (delta < 0) {
            System.out.println("NO SOLUTION");
        } else if (delta == 0) {
            double solution = -b / (2.0 * a);
            System.out.printf("One solution: %.2f\n", solution);
        } else {
            double x1 = (-b - Math.sqrt(delta)) / (2.0 * a);
            double x2 = (-b + Math.sqrt(delta)) / (2.0 * a);
            System.out.printf("Two solutions: %.2f and %.2f\n", x1, x2);
        }
    }
}
