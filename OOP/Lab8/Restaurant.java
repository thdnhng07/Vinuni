// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 08 – Week 09
// by Dat Thanh – V202401381
// Date: Apr 18, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                                 Restaurant
//-----------------------------------------------------------------------------

package Lab8;

import java.util.*;

class Dish {
    String name;
    int cost;

    Dish(String name, int cost) {
        this.name = name;
        this.cost = cost;
    }
}

class Customer {
    String name;
    int account;package Lab8;

    import java.util.*;
    
    class Dish {
        String name;
        int cost;
    
        Dish(String name, int cost) {
            this.name = name;
            this.cost = cost;
        }
    };
    
    class Customer {
        String name;
        int account;
        String boughtDish = null;
    
        Customer(String name, int account) {
            this.name = name;
            this.account = account;
        }
    };
    
    public class Restaurant {
    
        Queue<Dish> dishes;
        Queue<Customer> customers;
    
        public Restaurant() {
            dishes = new LinkedList<>();
            customers = new LinkedList<>();
        }
    
        public void readDishes(Scanner sc) {
            System.out.print("Enter the number of dish(s): ");
            int num = Integer.parseInt(sc.nextLine());
    
            for (int i = 1; i <= num; i++) {
                System.out.printf("Enter dish %d (<name> <cost>): ", i);
                String[] parts = sc.nextLine().split(" ");
                int cost = Integer.parseInt(parts[parts.length - 1]);
                String name = String.join(" ", Arrays.copyOfRange(parts, 0, parts.length - 1));
                dishes.add(new Dish(name, cost));
            }
        }
    
        public void readCustomers(Scanner sc) {
            System.out.print("Enter the number of waiting customer(s): ");
            int num = Integer.parseInt(sc.nextLine());
    
            for (int i = 1; i <= num; i++) {
                System.out.printf("Enter customer %d (<name> <account>): ", i);
                String[] parts = sc.nextLine().split(" ");
                int account = Integer.parseInt(parts[parts.length - 1]);
                String name = String.join(" ", Arrays.copyOfRange(parts, 0, parts.length - 1));
                customers.add(new Customer(name, account));
            }
        }
    
        public void processOrders() {
            Queue<Customer> finalCustomers = new LinkedList<>();
            Queue<Customer> remainingCustomers = new LinkedList<>(customers);
    
            int totalDishes = dishes.size();
            for (int i = 0; i < totalDishes; i++) {
                Dish currentDish = dishes.poll(); 
                boolean bought = false;
                int attempts = customers.size();
    
                while (attempts-- > 0) {
                    Customer c = customers.poll();
    
                    if (c.account >= currentDish.cost && !bought) {
                        c.account -= currentDish.cost;
                        c.boughtDish = currentDish.name;
                        finalCustomers.add(c);
                        System.out.println(c.name + " bought " + currentDish.name + "!");
                        bought = true;
                        break;
                    } else {
                        customers.add(c);
                    }
                }
    
                if (!bought) {

                }
    
                dishes.add(currentDish);
            }
    
            for (Customer c : customers) {
                finalCustomers.add(c);
            }
    

            for (Customer c : finalCustomers) {
                if (c.boughtDish == null) {
                    System.out.println(c.name + " didn't have enough money for any dish!");
                }
            }
        }
    
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            Restaurant testObj = new Restaurant();
    
            testObj.readDishes(sc);
            testObj.readCustomers(sc);
            testObj.processOrders();
    
            sc.close();
        }
    }
    

    Customer(String name, int account) {
        this.name = name;
        this.account = account;
    }
}

public class Restaurant {

    Queue<Dish> dishes;
    Queue<Customer> customers;

    public Restaurant() {
        dishes = new LinkedList<>();
        customers = new LinkedList<>();
    }

    public void readDishes(Scanner sc) {
        System.out.printf("Enter the number of dish(s): ");
        int numDishes = sc.nextInt();
        sc.nextLine();
        for (int i = 1; i <= numDishes; i++) {
            System.out.printf("Enter dish %d (<<name>> <<cost>>): ", i);
            String name = sc.nextLine();
            int cost = sc.nextInt();
            sc.nextLine();
            dishes.add(new Dish(name, cost));
        }
    }

    public void readCustomers(Scanner sc) {
        System.out.printf("Enter the number of waiting customer(s): ");
        int numCustomers = sc.nextInt();
        sc.nextLine();
        for (int i = 1; i <= numCustomers; i++) {
            System.out.printf("Enter customer %d (<<name>> <<account>>): ", i);
            String name = sc.nextLine();
            int account = sc.nextInt();
            sc.nextLine();
            customers.add(new Customer(name, account));
        }
    }

    public void processOrders() {

        while (!dishes.isEmpty()) {
            Dish currentDish = dishes.poll();
            int initialCustomerCount = customers.size();
            boolean dishSold = false;
            Queue<Customer> tempQueue = new LinkedList<>();


            for (int i = 0; i < initialCustomerCount; i++) {
                Customer currentCustomer = customers.poll();
                if (currentCustomer.account >= currentDish.cost) {

                    System.out.printf("%s bought %s!\n", currentCustomer.name, currentDish.name);
                    dishSold = true;
                    break;
                } else {

                    tempQueue.add(currentCustomer);
                }
            }


            customers.addAll(tempQueue);

            if (!dishSold && !customers.isEmpty()) {

                continue;
            }
        }


        while (!customers.isEmpty()) {
            Customer currentCustomer = customers.poll();
            System.out.printf("%s didn't have enough money for any dish!\n", currentCustomer.name);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Restaurant testObj = new Restaurant();

        testObj.readDishes(sc);
        testObj.readCustomers(sc);
        testObj.processOrders();

        sc.close();
    }
}