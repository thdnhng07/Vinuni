// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 04 – Week 04
// by Dat Thanh – V202401381
// Date: Mar 14, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                                Moving Object
//-----------------------------------------------------------------------------
package Lab4;

import java.util.Scanner;
import java.util.ArrayList;

class Object {
    private int x, y;

    public Object(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void moveLeft() {
        this.x--;
    }

    public void moveRight() {
        this.x++;
    }

    public void moveUp() {
        this.y++;
    }

    public void moveDown() {
        this.y--;
    }

    public void printLocation() {
        System.out.println(x + " " + y);
    }
}

public class MovingObject {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int x = scanner.nextInt(), y = scanner.nextInt();
        scanner.nextLine();

        Object obj = new Object(x, y);
        ArrayList<String> commands = new ArrayList<>();

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine().trim();
            if (line.equals("#")) break;
            commands.add(line);
        }

        for (String command : commands) {
            switch (command) {
                case "MOVE_LEFT": obj.moveLeft(); break;
                case "MOVE_RIGHT": obj.moveRight(); break;
                case "MOVE_UP": obj.moveUp(); break;
                case "MOVE_DOWN": obj.moveDown(); break;
            }
        }

        obj.printLocation();
        scanner.close();
    }
}
