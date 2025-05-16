// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 08 – Week 09
// by Dat Thanh – V202401381
// Date: Apr 18, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                             Bracket Sequence
//-----------------------------------------------------------------------------

package Lab8;

import java.util.*;

public class BracketSequence {

    private String bracketSeq;

    public BracketSequence() {
        bracketSeq = "";
    }

    public BracketSequence(String s) {
        bracketSeq = s;
    }

    public boolean isSupported() {

        for (char c : bracketSeq.toCharArray()) {
            if (c != '(' && c != ')' && c != '{' && c != '}' && c != '[' && c != ']') {
                return false;
            }
        }
        return true;
    }

    public boolean isValid() {
        Stack<Character> s = new Stack<Character>();
        boolean ok = true;

        for (char c : bracketSeq.toCharArray()) {

            if (c == '(' || c == '{' || c == '[') {
                s.push(c);
            }

            else if (c == ')' || c == '}' || c == ']') {
                if (s.isEmpty()) {
                    return false;
                }
                char top = s.pop();

                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }

        return ok && s.isEmpty();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String seq;
        int cnt = 0;

        while (true) {
            System.out.print("\nEnter a bracket sequence: ");
            seq = sc.nextLine();

            BracketSequence bs = new BracketSequence(seq);

            if (!bs.isSupported()) {
                System.out.println(seq + " is NOT supported (terminated)!");
                break;
            }

            if (!bs.isValid()) {
                System.out.println(seq + " is an INVALID bracket sequence!!!");
            } else {
                System.out.println(seq + " is a VALID bracket sequence.");
            }

            if (cnt++ > 5) {
                break;
            }
        }

        sc.close();
    }
}