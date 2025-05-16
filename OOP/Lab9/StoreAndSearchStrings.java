// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 09 – Week 10
// by Dat Thanh – V202401381
// Date: Apr 25, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                          Store And Search String
//-----------------------------------------------------------------------------
package Lab9;

import java.util.*;

class TreeNode {
    String key;
    TreeNode left, right;

    public TreeNode(String item) {
        key = item;
        left = right = null;
    }
}

class StringBST {
    private TreeNode root;

    public StringBST() {
        root = null;
    }

    public int insert(String key) {
        if (root == null) {
            root = new TreeNode(key);
            return 1;
        } else {
            return insertRec(root, key);
        }
    }

    private int insertRec(TreeNode node, String key) {
        int cmp = key.compareTo(node.key);
        if (cmp == 0) {
            return 0; // already exists
        } else if (cmp < 0) {
            if (node.left == null) {
                node.left = new TreeNode(key);
                return 1;
            } else {
                return insertRec(node.left, key);
            }
        } else {
            if (node.right == null) {
                node.right = new TreeNode(key);
                return 1;
            } else {
                return insertRec(node.right, key);
            }
        }
    }

    public int find(String key) {
        return findRec(root, key);
    }

    private int findRec(TreeNode node, String key) {
        if (node == null) {
            return 0;
        }
        int cmp = key.compareTo(node.key);
        if (cmp == 0) {
            return 1;
        } else if (cmp < 0) {
            return findRec(node.left, key);
        } else {
            return findRec(node.right, key);
        }
    }
}

public class StoreAndSearchStrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBST tree = new StringBST();
        List<String> output = new ArrayList<>();
        boolean readingInitialKeys = true;

        while (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.equals("*")) {
                readingInitialKeys = false;
                continue;
            }

            if (line.equals("***")) {
                break;
            }

            if (readingInitialKeys) {
                tree.insert(line);
            } else {
                String[] parts = line.split("\\s+");
                if (parts.length == 2) {
                    String cmd = parts[0];
                    String key = parts[1];
                    if (cmd.equals("insert")) {
                        output.add(String.valueOf(tree.insert(key)));
                    } else if (cmd.equals("find")) {
                        output.add(String.valueOf(tree.find(key)));
                    }
                }
            }
        }

        sc.close();

        for (String result : output) {
            System.out.println(result);
        }
    }
}

