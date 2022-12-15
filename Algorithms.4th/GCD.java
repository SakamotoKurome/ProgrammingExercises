/*
 * P14
 */

public class GCD {
    // 欧几里德算法
    public static int gcd(int p, int q) {
        if (q == 0)
            return p;
        int r = p % q;
        System.out.println(r);
        return gcd(q, r);
    }

    public static void main(String[] args) {
        System.out.println(GCD.gcd(1034, 893));
    }

}
