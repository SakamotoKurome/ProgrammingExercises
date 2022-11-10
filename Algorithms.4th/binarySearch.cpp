#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

class BinarySearch
{
public:
    // 二分查找算法
    static int indexOf(int *a, int n, int key)
    {
        int lo = 0;
        int hi = n - 1;
        while (lo <= hi)
        {
            int mid = lo + ((hi - lo) >> 2);
            if (key < a[mid])
            {
                hi = mid - 1;
            }
            else if (key > a[mid])
            {
                lo = mid + 1;
            }
            else
            {
                return mid;
            }
        }
        return -1;
    }
};

int main(int argc, char *argv[])
{
    // 读取从命令行获取的文件名
    std::freopen(argv[1], "r", stdin);
    int n;
    std::vector<int> allowlist;
    while (std::cin >> n)
    {
        allowlist.emplace_back(n);
    }
    std::fclose(stdin);
    // 从小到大排序
    std::sort(allowlist.begin(), allowlist.end());
    // 转换为数组
    n = allowlist.size();
    int allowlist_c[n];
    for (int i = 0; i < n; ++i)
    {
        allowlist_c[i] = allowlist.at(i);
    }
    // 在有序列表中查找命令行余下的数字
    for (int i = 2; i < argc; ++i)
    {
        int key = std::stoi(argv[i], nullptr);
        if (BinarySearch::indexOf(allowlist_c, n, key) == -1)
        {
            std::cout << key << std::endl;
        }
    }
    return 0;
}