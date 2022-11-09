import { argv } from 'node:process';
import { open } from 'node:fs/promises';

/*
 * node binarySearch.js tinyAllowlist.txt 83 84
 */

class BinarySearch {
    // 二分查找算法
    static indexOf(a, key) {
        let lo = 0;
        let hi = a.length - 1;
        while (lo <= hi) {
            const mid = lo + (hi - lo) / 2;
            if (key < a[mid]) {
                hi = mid - 1;
            } else if (key > a[mid]) {
                lo = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}

// 读取从命令行获取的文件名
const f = await open(argv[2]);
let allowlist = [];
for await (const line of f.readLines()) {
    allowlist.push(Number(line))
}
// 从小到大排序
allowlist.sort((a, b) => a - b)
// 在有序列表中查找命令行余下的数字
for (let i = 3; i < argv.length; i++) {
    const key = argv[i];
    if (BinarySearch.indexOf(allowlist, key) == -1) {
        console.log(key);
    }
}