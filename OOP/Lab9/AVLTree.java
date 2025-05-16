// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 09 – Week 10
// by Dat Thanh – V202401381
// Date: Apr 25, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                                  AVL Tree
//-----------------------------------------------------------------------------
package Lab9;

import java.util.*;

class Node {
    int key, height;
    Node left, right;

    Node(int key) {
        this.key = key;
        this.height = 1;
    }
}

class AVLTree {
    Node root;

    int height(Node node) {
        return (node == null) ? 0 : node.height;
    }

    int max(int a, int b) {
        return (a > b) ? a : b;
    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update heights
        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;

        return x;
    }

    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update heights
        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;

        return y;
    }

    int getBalance(Node node) {
        return (node == null) ? 0 : height(node.left) - height(node.right);
    }

    Node insert(Node node, int key) {
        if (node == null)
            return new Node(key);

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else
            return node; // duplicates not allowed

        node.height = 1 + max(height(node.left), height(node.right));
        int balance = getBalance(node);

        // Left Left Case
        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        // Right Right Case
        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        // Left Right Case
        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        // Right Left Case
        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    Node minValueNode(Node node) {
        Node current = node;
        while (current.left != null)
            current = current.left;
        return current;
    }

    Node delete(Node root, int key) {
        if (root == null)
            return root;

        if (key < root.key)
            root.left = delete(root.left, key);
        else if (key > root.key)
            root.right = delete(root.right, key);
        else {
            if ((root.left == null) || (root.right == null)) {
                Node temp = (root.left != null) ? root.left : root.right;
                if (temp == null) {
                    root = null;
                } else {
                    root = temp;
                }
            } else {
                Node temp = minValueNode(root.right);
                root.key = temp.key;
                root.right = delete(root.right, temp.key);
            }
        }

        if (root == null)
            return root;

        root.height = max(height(root.left), height(root.right)) + 1;
        int balance = getBalance(root);

        // Left Left Case
        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);

        // Left Right Case
        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }

        // Right Right Case
        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);

        // Right Left Case
        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }

        return root;
    }

    public void insert(int key) {
        root = insert(root, key);
    }

    public void delete(int key) {
        root = delete(root, key);
    }

    void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.key + " ");
            inOrder(node.right);
        }
    }

    void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    void postOrder(Node node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            System.out.print(node.key + " ");
        }
    }

    public static void main(String[] args) {
        AVLTree tree = new AVLTree();
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            String input = scanner.nextLine().trim();
            if (input.equals("#")) {
                running = false;
                continue;
            }

            String[] parts = input.split("\\s+");
            if (parts.length == 0) continue;

            String command = parts[0].toLowerCase();
            try {
                switch (command) {
                    case "insert":
                        if (parts.length != 2) {
                            System.out.println("Invalid insert command. Use 'insert <key>'.");
                            break;
                        }
                        int insertKey = Integer.parseInt(parts[1]);
                        tree.insert(insertKey);
                        System.out.println("Inserted key: " + insertKey);
                        break;

                    case "delete":
                        if (parts.length != 2) {
                            System.out.println("Invalid delete command. Use 'delete <key>'.");
                            break;
                        }
                        int deleteKey = Integer.parseInt(parts[1]);
                        tree.delete(deleteKey);
                        System.out.println("Deleted key: " + deleteKey);
                        break;

                    case "inorder":
                        System.out.print("Inorder traversal: ");
                        tree.inOrder(tree.root);
                        System.out.println();
                        break;

                    case "preorder":
                        System.out.print("Preorder traversal: ");
                        tree.preOrder(tree.root);
                        System.out.println();
                        break;

                    case "postorder":
                        System.out.print("Postorder traversal: ");
                        tree.postOrder(tree.root);
                        System.out.println();
                        break;

                    default:
                        System.out.println("Unknown command.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid key. Please enter an integer.");
            }
        }

        scanner.close();
    }
}

