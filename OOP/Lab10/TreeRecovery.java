// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 10 – Week 12
// by Dat Thanh – V202401381
// Date: May 09, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                          	  Tree Recovery
//-----------------------------------------------------------------------------
// package cscorner;


import java.util.*;

public class TreeRecovery {

    int n;

    int[] pre, in;

    int[] left, right;

    HashMap<Integer, Integer> valueToIndex; // map node value to index

    int[] indexToValue; // map index to node value

    void readOrders(Scanner sc) {
        System.out.printf("Enter the number of node:\n");
        n = sc.nextInt();
        
        pre = new int[n];
        System.out.print("Enter the preorder traversal:\n");
        for (int i = 0; i < n; i++)
            pre[i] = sc.nextInt();
        
        in = new int[n];
        System.out.print("Enter the inorder traversal:\n");
        for (int i = 0; i < n; i++)
            in[i] = sc.nextInt();

        // Build value to index mapping
        valueToIndex = new HashMap<>();
        indexToValue = new int[n];
        for (int i = 0; i < n; i++) {
            valueToIndex.put(in[i], i);
            indexToValue[i] = in[i];
        }
    }

    int getRoot(int lowIn, int highIn, int lowPre, int highPre) {
        if (lowIn > highIn)
            return -1; // empty subtree
        int rootVal = pre[lowPre];
        // find root in inorder
        int idx = lowIn;
        while (idx <= highIn && in[idx] != rootVal) idx++;
        int leftSize = idx - lowIn;
        // recursively build left and right subtrees
        int leftChild = getRoot(lowIn, idx - 1, lowPre + 1, lowPre + leftSize);
        int rightChild = getRoot(idx + 1, highIn, lowPre + leftSize + 1, highPre);
        int rootIdx = valueToIndex.get(rootVal);
        left[rootIdx] = leftChild == -1 ? -1 : valueToIndex.get(pre[lowPre + 1]);
        if (leftChild == -1) left[rootIdx] = -1;
        right[rootIdx] = rightChild == -1 ? -1 : valueToIndex.get(pre[lowPre + leftSize + 1]);
        if (rightChild == -1) right[rootIdx] = -1;
        return rootVal;
    }

    void printArr(int[] arr, int n) {
        for (int i = 0; i < n; i++)
            System.out.print((arr[i] == -1 ? -1 : indexToValue[arr[i]]) + " ");
        System.out.println();
    }

    void findTree() {
        left = new int[n];
        right = new int[n];
        Arrays.fill(left, -1);
        Arrays.fill(right, -1);
        getRoot(0, n - 1, 0, n - 1);

        System.out.print("Left child : ");
        this.printArr(left, n);
        System.out.print("Right child: ");
        this.printArr(right, n);
        
        for (int i = 0; i < n; i++) {
            String res = "Node " + indexToValue[i] + " has ";
            if (left[i] != -1)
                res += "left child " + indexToValue[left[i]];
            else
                res += "no left child";
            res += " and ";
            if (right[i] != -1)
                res += "right child " + indexToValue[right[i]];
            else
                res += "no right child";
            res += ".\n";
            System.out.print(res);
        }
    }

    public static void main(String[] argv) {
        Scanner sc = new Scanner(System.in);
        TreeRecovery tr = new TreeRecovery();
        System.out.println("INPUT:");
        tr.readOrders(sc);
        System.out.println("OUTPUT:");
        tr.findTree();
        sc.close();
    }
}