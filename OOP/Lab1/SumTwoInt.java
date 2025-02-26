//VinUniversity, Spring 2025

//COMP1020 Object-Oriented Programming and Data Structures

//Lab 01 – Week 01 – Getting started with Java

//by Dat Thanh – V202401381

//Date: Feb 21, 2025

//Disclaimer: I certify that this assignment is my own work and that I have not copied in part

//or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------

//                                         Sum of Two Integers

//-----------------------------------------------------------------------------
package Lab1;

import java.util.Scanner;

public class SumTwoInt {
    public static void main(String[] args){
        Scanner my_Obj = new Scanner(System.in);

        int a = my_Obj.nextInt();
        int b = my_Obj.nextInt();

        System.out.println(a + b);

        my_Obj.close();
    }
}
