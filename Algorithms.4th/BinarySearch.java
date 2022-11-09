import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

/*
 * P18
 * Java 程序及其命令行的调用
 * java BinarySearch tinyAllowlist.txt 83 84
 */

public class BinarySearch {
    // 二分查找算法
    public static int indexOf(int[] a, int key) {
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (key < a[mid])
                hi = mid - 1;
            else if (key > a[mid])
                lo = mid + 1;
            else
                return mid;
        }
        return -1;
    }

    // list 转 int 数组
    public static int[] convertIntegers(List<Integer> integers) {
        int[] ret = new int[integers.size()];
        Iterator<Integer> iterator = integers.iterator();
        for (int i = 0; i < ret.length; i++) {
            ret[i] = iterator.next().intValue();
        }
        return ret;
    }

    public static void main(String[] args) {
        try {
            // 读取从命令行获取的文件名
            Scanner scanner = new Scanner(new File(args[0]));
            ArrayList<Integer> allowlist = new ArrayList<>();
            while (scanner.hasNextInt()) {
                allowlist.add(scanner.nextInt());
            }
            // 从小到大排序
            Collections.sort(allowlist);
            // 转换为数组
            int[] allowlist_c = convertIntegers(allowlist);
            // 在有序列表中查找命令行余下的数字
            for (int i = 1; i < args.length; i++) {
                int key = Integer.parseInt(args[i]);
                if (BinarySearch.indexOf(allowlist_c, key) == -1) {
                    System.out.println(key);
                }
            }
        } catch (Exception e) {
            System.out.println(e.toString());
        }

    }
}
