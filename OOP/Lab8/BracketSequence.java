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
        // Check if the string contains only supported bracket symbols
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
            // If it's an opening bracket, push onto stack
            if (c == '(' || c == '{' || c == '[') {
                s.push(c);
            }
            // If it's a closing bracket, check for matching opening bracket
            else if (c == ')' || c == '}' || c == ']') {
                if (s.isEmpty()) {
                    return false; // No matching opening bracket
                }
                char top = s.pop();
                // Check if brackets match
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false; // Mismatched brackets
                }
            }
        }
        // Sequence is valid only if stack is empty (all brackets matched)
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