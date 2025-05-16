
// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 10 – Week 12
// by Dat Thanh – V202401381
// Date: May 09, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                          	  ER Help Desk
//-----------------------------------------------------------------------------
// package cscorner;

import java.util.Scanner;

class Node {
    int key;
    String patientID;
    int height;
    Node left, right;

    Node(int key, String patientID) {
        this.key = key;
        this.patientID = patientID;
        this.height = 1;
    }
}

class PatientPriorityQueue {
    Node root;

    int height(Node node) {
        return node == null ? 0 : node.height;
    }

    int getBalance(Node node) {
        return node == null ? 0 : height(node.left) - height(node.right);
    }
    
    int max(int a, int b) {
      return (a > b) ? a : b;
    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        x.right = y;
        y.left = T2;

        y.height = 1 + max(height(y.left), height(y.right));
        x.height = 1 + max(height(x.left), height(x.right));

        return x;
    }

    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        y.left = x;
        x.right = T2;

        x.height = 1 + max(height(x.left), height(x.right));
        y.height = 1 + max(height(y.left), height(y.right));

        return y;
    }

    Node insert(Node node, int key, String patientID) {
        if (node == null)
            return new Node(key, patientID);

        if (key < node.key)
            node.left = insert(node.left, key, patientID);
        else if (key > node.key)
            node.right = insert(node.right, key, patientID);
        else
            return node;

        node.height = 1 + max(height(node.left), height(node.right));
        int balance = getBalance(node);

        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    Node delete(Node node, int key) {
        if (node == null)
            return node;

        if (key < node.key)
            node.left = delete(node.left, key);
        else if (key > node.key)
            node.right = delete(node.right, key);
        else {
            if (node.left == null || node.right == null) {
                Node temp = node.left != null ? node.left : node.right;
                if (temp == null) {
                    node = null;
                } else {
                    node = temp;
                }
            } else {
                Node temp = minValueNode(node.right);
                node.key = temp.key;
                node.patientID = temp.patientID;
                node.right = delete(node.right, temp.key);
            }
        }

        if (node == null)
            return node;

        node.height = 1 + max(height(node.left), height(node.right));
        int balance = getBalance(node);

        if (balance > 1 && getBalance(node.left) >= 0)
            return rightRotate(node);

        if (balance > 1 && getBalance(node.left) < 0) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        if (balance < -1 && getBalance(node.right) <= 0)
            return leftRotate(node);

        if (balance < -1 && getBalance(node.right) > 0) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    Node minValueNode(Node node) {
        while (node.left != null)
            node = node.left;
        return node;
    }

    Node maxValueNode(Node node) {
        while (node.right != null)
            node = node.right;
        return node;
    }

    Node search(Node node, int key) {
        if (node == null || node.key == key)
            return node;
        return (key < node.key) ? search(node.left, key) : search(node.right, key);
    }

    void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.println(node.patientID + " – Priority: " + node.key);
            inOrder(node.right);
        }
    }

    public void insert(int key, String patientID) {
        root = insert(root, key, patientID);
    }

    public boolean delete(int key) {
        if (search(root, key) != null) {
            root = delete(root, key);
            return true;
        }
        return false;
    }

    public Node findLowest() {
        return minValueNode(root);
    }

    public Node findHighest() {
        return maxValueNode(root);
    }

    public void listPatients() {
        if (root == null)
            System.out.println("No patients in the system.");
        else
            inOrder(root);
    }
}

public class ERHelpDesk {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PatientPriorityQueue queue = new PatientPriorityQueue();

        while (sc.hasNextLine()) {
            String input = sc.nextLine().trim();
            if (input.equals("#")) {
                System.out.println("System shutting down.");
                break;
            }

            String[] parts = input.split("\\s+");
            if (parts.length == 0) continue;

            String command = parts[0].toLowerCase();

            switch (command) {
                case "add":
                    if (parts.length != 3) {
                        System.out.println("Invalid add command.");
                        break;
                    }
                    try {
                        int priority = Integer.parseInt(parts[1]);
                        String id = parts[2];
                        queue.insert(priority, id);
                        System.out.println("Added patient " + id + " with priority " + priority + ".");
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid priority.");
                    }
                    break;

                case "treat":
                    if (parts.length != 2) {
                        System.out.println("Invalid treat command.");
                        break;
                    }
                    try {
                        int priority = Integer.parseInt(parts[1]);
                        if (queue.delete(priority)) {
                            System.out.println("Treated patient with priority " + priority + ".");
                        } else {
                            System.out.println("No patient found with priority " + priority + ".");
                        }
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid priority.");
                    }
                    break;

                case "highest":
                    Node high = queue.findHighest();
                    if (high != null)
                        System.out.println(high.patientID + " – Priority: " + high.key);
                    else
                        System.out.println("No patients in the system.");
                    break;

                case "lowest":
                    Node low = queue.findLowest();
                    if (low != null)
                        System.out.println(low.patientID + " – Priority: " + low.key);
                    else
                        System.out.println("No patients in the system.");
                    break;

                case "list":
                    queue.listPatients();
                    break;

                default:
                    System.out.println("Unknown command.");
            }
        }

        sc.close();
    }
}
