#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>

// 二分查找算法
int binarySearch(int t_key, std::vector<int> t_a)
{
    int lo = 0;
    int hi = t_a.size() - 1;
    while (lo <= hi)
    {
        int mid = lo + ((hi - lo) >> 2);
        if (t_key < t_a.at(mid))
        {
            hi = mid - 1;
        }
        else if (t_key > t_a.at(mid))
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

int main(int argc, char *argv[])
{
    // 读取从命令行获取的文件名
    std::freopen(argv[1], "r", stdin);
    int n;
    std::vector<int> whitelist;
    while (std::cin >> n)
    {
        whitelist.emplace_back(n);
    }
    std::fclose(stdin);
    // 从小到大排序
    std::sort(whitelist.begin(), whitelist.end());
    // 在有序列表中查找命令行余下的数字
    for (int i = 2; i < argc; ++i)
    {
        int key = std::stoi(argv[i], nullptr);
        if (binarySearch(key, whitelist) == -1)
        {
            std::cout << key << std::endl;
        }
    }
    return 0;
}