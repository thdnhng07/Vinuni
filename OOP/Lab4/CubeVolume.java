// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 04 – Week 04
// by Dat Thanh – V202401381
// Date: Mar 14, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                                 Cobe Volume
//-----------------------------------------------------------------------------
package Lab4;

import java.util.Scanner;

class RectangularPrism {
    protected double length, width, height;

    public RectangularPrism(double length, double width, double height) {
        this.length = length;
        this.width = width;
        this.height = height;
    }

    public double getSurfaceArea() {
        return 2 * (length * width + width * height + height * length);
    }

    public double getVolume() {
        return length * width * height;
    }
}

class CubeVolumecalc extends RectangularPrism {
    private String color;

    public CubeVolumecalc(double side, String color) {
        super(side, side, side);
        this.color = color;
    }

    public void printColor() {
        System.out.println("The cube is " + color);
    }

    public void cubeInformation() {
        System.out.println("Cube's detail:");
        System.out.printf("length: %.2f\nwidth: %.2f\nheight: %.2f\n", length, width, height);
        System.out.println("Computing the surface area...");
        System.out.printf("The surface area of the cube is %.2f\n", getSurfaceArea());
        System.out.println("Computing the volume...");
        System.out.printf("The volume of the cube is %.2f\n", getVolume());
        printColor();
    }
}

public class CubeVolume {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Case 1. Enter a space key to create a cube with length 1.00 and color blue, or");
        System.out.println("Case 2. Enter one number to create a cube with length s and color blue, or");
        System.out.println("Case 3. Enter a number and a color to create a cube with length s and color c:");

        String input = scanner.nextLine().trim();

        double length = 1.00;
        String color = "blue";

        if (!input.isEmpty()) {
            Scanner lineScanner = new Scanner(input);
            if (lineScanner.hasNextDouble()) {
                length = lineScanner.nextDouble();
                if (lineScanner.hasNext()) {
                    color = lineScanner.next();
                }
            }
            lineScanner.close();
        }

        CubeVolumecalc cube = new CubeVolumecalc(length, color);
        cube.cubeInformation();

        scanner.close();
    }
}
