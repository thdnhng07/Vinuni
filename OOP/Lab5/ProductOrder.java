// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 05 – Week 05
// by Dat Thanh – V202401381
// Date: Mar 21, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.
//----------------------------------Problem 1-------------------------------
//                                Product Order
//-----------------------------------------------------------------------------
package Lab5;

import java.util.Scanner;

class Order {
    private int[] productIds;
    private String[] productNames;
    private double[] productPrices;

    // Constructor
    public Order(int numProducts, Scanner scanner) {
        productIds = new int[numProducts];
        productNames = new String[numProducts];
        productPrices = new double[numProducts];

        System.out.println("Enter product details (ID, Name, Price):");

        for (int i = 0; i < numProducts; i++) {
            productIds[i] = scanner.nextInt();
            productNames[i] = scanner.next();
            productPrices[i] = scanner.nextDouble();
        }
    }

    // TODO
    private int getProductIndex(int productId) {
        for (int i = 0; i < productIds.length; i++) {
            if (productIds[i] == productId) {
                return i;
            }
        }
        return -1;
    }

    // TODO
    public void placeOrder(int productId, int quantity) {
        int index = getProductIndex(productId);
        if (index == -1) {
            System.out.println("Invalid Product ID");
            return;
        }

        double totalPrice = productPrices[index] * quantity;
        System.out.println("Order placed: " + quantity + " x " + productNames[index] +
                " | Total: $" + totalPrice);
    }
    // TODO
    public void placeOrder(int productId, int quantity, double discountPercent) {
        int index = getProductIndex(productId);
        if (index == -1) {
            System.out.println("Invalid Product ID");
            return;
        }

        double totalPrice = productPrices[index] * quantity;
        double discountedPrice = totalPrice - (totalPrice * discountPercent / 100);
        System.out.println("Order placed: " + quantity + " x " + productNames[index] +
                " | Total after discount: $" + discountedPrice);
    }
}

public class ProductOrder {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // TODO
        int numProducts = scanner.nextInt();
        Order order = new Order(numProducts, scanner);

        // TODO
        System.out.println("Enter order type (1 = Without Discount, 2 = With Discount): ");
        int orderType = scanner.nextInt();

        if (orderType == 1) {
            int productId = scanner.nextInt();
            int quantity = scanner.nextInt();
            order.placeOrder(productId, quantity);
        } else if (orderType == 2) {
            int productId = scanner.nextInt();
            int quantity = scanner.nextInt();
            double discountPercent = scanner.nextDouble();
            order.placeOrder(productId, quantity, discountPercent);
        } else {
            System.out.println("Error: Invalid order type");
        }

        scanner.close();
    }
}
