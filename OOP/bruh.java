public class bruh {
    class Q3 {
        int x;
        Q3 (int x) {
        this.x = x*x;
        }
        static void m1(int a) {
        a = a/2;
        }
        static void m2(Test obj) {
        obj.x = - obj.x;
        }
        public static void main(String[] args) {
        int x = 10;
        m1(x);
        System.out.println("VinUni " + x);
        Test obj = new Q3 (x+20);
        m2(obj);
        }
}
}
