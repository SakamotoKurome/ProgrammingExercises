import { argv } from 'node:process';
import { open } from 'node:fs/promises';

// 二分查找算法
function binarySearch(key, a) {
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

// 读取从命令行获取的文件名
const file = await open(argv[2]);
let a = [];
for await (const line of file.readLines()) {
    a.push(Number(line))
}
// 从小到大排序
a.sort((a, b) => a - b)
// 在有序列表中查找命令行余下的数字
for (let i = 3; i < argv.length; i++) {
    const key = argv[i];
    if (binarySearch(key, a) == -1) {
        console.log(key);
    }
}