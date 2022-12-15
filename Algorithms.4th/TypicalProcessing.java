/*
 * P24
 * 典型的数组处理代码
 */

public class TypicalProcessing {
    // 最大值
    public static double max(double[] a) {
        double max = a[0];
        for (int i = 1; i < a.length; i++) {
            if (a[i] > max) {
                max = a[i];
            }
        }
        return max;
    }

    // 平均值
    public static double average(double[] a) {
        int N = a.length;
        double sum = 0.0;
        for (int i = 0; i < N; i++) {
            sum += a[i];
        }
        double average = sum / N;
        return average;
    }

    // 倒序
    public static void reverse(double[] a) {
        int N = a.length;
        for (int i = 0; i < N / 2; i++) {
            double temp = a[i];
            a[i] = a[N - 1 - i];
            a[N - 1 - i] = temp;
        }
    }

    // 牛顿法求平方根
    public static double sqrt(double c) {
        if (c < 0) {
            return Double.NaN;
        }
        double err = 1e-15;
        double t = c;
        while (Math.abs(t - c / t) > err * t) {
            t = (c / t + t) / 2.0;
        }
        return t;
    }

    public static void main(String[] args) {
        double[] a = { 413.23, 545.431, 246.23, 241.76, 754.45, 341.85 };
        System.out.println(TypicalProcessing.max(a));
        System.out.println(TypicalProcessing.average(a));
        TypicalProcessing.reverse(a);
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }
}