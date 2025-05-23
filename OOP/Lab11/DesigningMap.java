// VinUniversity, Spring 2025
// COMP1020 Object-Oriented Programming and Data Structures
// Lab 11 – Week 13
// by Dat Thanh – V202401381
// Date: May 23, 2025
// Disclaimer: I certify that this assignment is my own work and that I have not copied in part
// or whole or otherwise plagiarised the work of other students and/or persons.

//----------------------------------Problem 1-------------------------------
//                          	 Designing Map
//-----------------------------------------------------------------------------
import java.util.*;

public class DesigningMap {
    static final int MAX = 10; // Buildings numbered 0 through 9
    static final int INF = (int)1e9 + 7;
    static int[] dist = new int[MAX];
    static ArrayList<Node>[] graph = new ArrayList[MAX];

    // Each Node represents a neighbor building and the travel time
    static class Node implements Comparable<Node> {
        int id, weight;

        public Node(int id, int weight) {
            this.id = id;
            this.weight = weight;
        }

        @Override
        public int compareTo(Node other) {
            return this.weight - other.weight;
        }
    }

    // Dijkstra's algorithm to compute shortest travel times from s
    public static void Dijkstra(int s) {
        // Initialize distances
        Arrays.fill(dist, INF);
        dist[s] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(s, 0));

        while (!pq.isEmpty()) {
            Node current = pq.poll();
            int u = current.id;
            int w = current.weight;
            if (w > dist[u]) continue;

            for (Node neighbor : graph[u]) {
                int v = neighbor.id;
                int time = neighbor.weight;
                if (dist[u] + time < dist[v]) {
                    dist[v] = dist[u] + time;
                    pq.add(new Node(v, dist[v]));
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Initialize graph
        for (int i = 0; i < MAX; i++) {
            graph[i] = new ArrayList<>();
        }

        // Read number of roads
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int w = sc.nextInt();
            // Since roads are bidirectional:
            graph[a].add(new Node(b, w));
            graph[b].add(new Node(a, w));
        }

        // Read start building and compute shortest paths
        int c = sc.nextInt();
        Dijkstra(c);

        // Answer queries
        int q = sc.nextInt();
        for (int i = 0; i < q; i++) {
            int v = sc.nextInt();
            if (dist[v] != INF) {
                System.out.println(dist[v]);
            } else {
                System.out.println("NO PATH");
            }
        }

        sc.close();
    }
}
