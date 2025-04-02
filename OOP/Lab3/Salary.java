// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 03 – Week 04
// by Dat Thanh – V202401381
// Date: Feb 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 3-------------------------------
//                                   Salary
//-----------------------------------------------------------------------------
package Lab3;
import java.util.Scanner;
import java.util.ArrayList;

class Staff{
    protected int id, pv;

    public Staff(int id, int pv) {
        this.id = id;
        this.pv = pv;
    }

    public void updatePV(int pv) {
        this.pv = pv;
    }

    public int getSalary() {
        return 1000 * pv;
    }
}

class Teacher extends Staff{
    private int gd;

    public Teacher(int id, int pv, int gd) {
        super(id, pv);
        this.gd = gd;
    }
    public int getSalary() {
        return 1500 * pv + 2000 * gd;
    }
}

public class Salary{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        ArrayList<Staff> staffs = new ArrayList<>();

        while (scanner.hasNext()) {
            String command = scanner.next();
            if (command.equals("#")) break;

            if (command.equals("TEACHER")) {
                int id = scanner.nextInt();
                int pv = scanner.nextInt();
                int gd = scanner.nextInt();
                Teacher teacher = new Teacher(id, pv, gd);
                staffs.add(teacher);
            } else if (command.equals("STAFF")) {
                int id = scanner.nextInt();
                int pv = scanner.nextInt();
                Staff staff = new Staff(id, pv);
                staffs.add(staff);
            } else if (command.equals("UPDATE")){
                int id = scanner.nextInt();
                int pv = scanner.nextInt();
                for (Staff staff : staffs) {
                    if (staff.id == id) {
                        staff.updatePV(pv);
                        break;
                    }
                }
            } else if (command.equals("SALARY")){
                int id = scanner.nextInt();
                int salary = 0;
                for (Staff staff : staffs) {
                    if (staff.id == id){
                        salary = staff.getSalary();
                        break;
                    }
                }
                System.out.println(salary);
            }
        }
        scanner.close();
    }
}
