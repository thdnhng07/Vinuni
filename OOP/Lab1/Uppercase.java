//VinUniversity, Spring 2025

//COMP1020 Object-Oriented Programming and Data Structures

//Lab 01 – Week 01 – Getting started with Java

//by Dat Thanh – V202401381

//Date: Feb 21, 2025

//Disclaimer: I certify that this assignment is my own work and that I have not copied in part

//or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------

//                                         Turn input into Uppercase

//-----------------------------------------------------------------------------
package Lab1;

import java.util.Scanner;

public class Uppercase {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String Text = scanner.nextLine();
        System.out.println(Text.toUpperCase());

        scanner.close();
    }
    
}
