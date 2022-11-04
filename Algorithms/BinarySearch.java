import java.io.File;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class BinarySearch {
    // 二分查找算法
    public static int rank(int key, ArrayList<Integer> a) {
        int lo = 0;
        int hi = a.size() - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (key < a.get(mid))
                hi = mid - 1;
            else if (key > a.get(mid))
                lo = mid + 1;
            else
                return mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        try {
            // 读取从命令行获取的文件名
            Scanner scanner = new Scanner(new File(args[0]));
            ArrayList<Integer> whitelist = new ArrayList<>();
            while (scanner.hasNextInt()) {
                whitelist.add(scanner.nextInt());
            }
            // 从小到大排序
            Collections.sort(whitelist);
            // 在有序列表中查找命令行余下的数字
            for (int i = 1; i < args.length; i++) {
                int key = Integer.parseInt(args[i]);
                if (BinarySearch.rank(key, whitelist) == -1) {
                    System.out.println(key);
                }
            }
        } catch (Exception e) {
            System.out.println(e.toString());
        }

    }
}
