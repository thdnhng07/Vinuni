// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 03 – Week 04
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                                  Rectangle
//-----------------------------------------------------------------------------
package Lab3;
import java.util.Scanner;

class RectangleCalc {
    private final int length, width;

    public RectangleCalc(int length, int width) {
        this.length = length;
        this.width = width;
    }

    public int computeArea() {
        return length * width;
    }

    public int computePerimeter() {
        return 2 * (length + width);
    }
}

public class Rectangle {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            int length = scanner.nextInt();
            int width = scanner.nextInt();

            RectangleCalc rectangle = new RectangleCalc(length, width);
            System.out.println(rectangle.computeArea() + " " + rectangle.computePerimeter());
        }
    }
}
