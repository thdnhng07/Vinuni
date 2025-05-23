// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 11 – Week 13
// by Dat Thanh – V202401381
// Date: May 23, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 2-------------------------------
//                          	  City Planner
//-----------------------------------------------------------------------------
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Edge implements Comparable<Edge> {
    String v1;
    String v2;
    int weight;

    public Edge(String v1, String v2, int weight) {
        this.v1 = v1;
        this.v2 = v2;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge other) {
        return Integer.compare(this.weight, other.weight);
    }
}

class Subset {
    String parent;
    int rank;
}

class Graph {
    List<Edge> edges;
    List<String> nodes;
    int numOfVertices;

    public Graph() {
        this.edges = new ArrayList<>();
        this.nodes = new ArrayList<>();
        this.numOfVertices = 0;
    }

    public void addEdge(String v1, String v2, int weight) {
        edges.add(new Edge(v1, v2, weight));
        if (!nodes.contains(v1)) {
            nodes.add(v1);
            numOfVertices++;
        }
        if (!nodes.contains(v2)) {
            nodes.add(v2);
            numOfVertices++;
        }
    }

    public String find(Subset[] subsets, String vertex) {
        int i = nodes.indexOf(vertex);
        if (!subsets[i].parent.equals(vertex)) {
            subsets[i].parent = find(subsets, subsets[i].parent);
        }
        return subsets[i].parent;
    }

    public void union(Subset[] subsets, String x, String y) {
        String xroot = find(subsets, x);
        String yroot = find(subsets, y);
        int xIndex = nodes.indexOf(xroot);
        int yIndex = nodes.indexOf(yroot);

        if (subsets[xIndex].rank < subsets[yIndex].rank) {
            subsets[xIndex].parent = yroot;
        } else if (subsets[xIndex].rank > subsets[yIndex].rank) {
            subsets[yIndex].parent = xroot;
        } else {
            subsets[yIndex].parent = xroot;
            subsets[xIndex].rank++;
        }
    }

    public void findMST() {
        Edge[] result = new Edge[numOfVertices];
        int e = 0;
        int i = 0;

        Collections.sort(edges);

        Subset[] subsets = new Subset[numOfVertices];
        for (int v = 0; v < numOfVertices; v++) {
            subsets[v] = new Subset();
            subsets[v].parent = nodes.get(v);
            subsets[v].rank = 0;
        }

        while (e < numOfVertices - 1) {
            Edge nextEdge = edges.get(i++);
            String x = find(subsets, nextEdge.v1);
            String y = find(subsets, nextEdge.v2);

            if (!x.equals(y)) {
                result[e++] = nextEdge;
                union(subsets, x, y);
            }
        }

        System.out.println("The plan to upgrade is as follows:");
        int minCost = 0;
        for (i = 0; i < e; i++) {
            System.out.println(String.format(
                "- %-15s <--> %-17s | Cost: %d", 
                result[i].v1, result[i].v2, result[i].weight));
            minCost += result[i].weight;
        }
        System.out.println("The MST has the Minimum Cost of " + minCost);
    }
}

public class CityPlanner {
    public static void main(String[] args) {
        Graph g = new Graph();
        g.addEdge("Olympics Center", "North Hotel", 12);
        g.addEdge("Olympics Center", "Park", 9);
        g.addEdge("Olympics Center", "Beach", 18);
        g.addEdge("North Hotel", "Park", 5);
        g.addEdge("North Hotel", "Central Mall", 11);
        g.addEdge("Park", "City Center", 22);
        g.addEdge("City Center", "Central Mall", 19);
        g.addEdge("City Center", "Movie Theatre", 8);
        g.addEdge("City Center", "Beach", 7);
        g.addEdge("City Center", "South Hotel", 17);
        g.addEdge("Beach", "South Hotel", 6);
        g.addEdge("Movie Theatre", "South Hotel", 3);
        g.addEdge("Movie Theatre", "Airport", 20);
        g.addEdge("North Hotel", "Conference Center", 10);
        g.addEdge("Movie Theatre", "Conference Center", 15);
        g.addEdge("Airport", "Conference Center", 16);
        g.findMST();
    }
}
