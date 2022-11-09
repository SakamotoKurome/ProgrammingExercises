#include <iostream>

void bucketSort()
{
}

int main()
{
    int book[1001];
    for (int i = 0; i < 1001; ++i)
    {
        book[i] = 0;
    }
    int n, t;
    std::cin >> n;
    for (int i = 1; i <= n; ++i)
    {
        std::cin >> t;
        book[t]++;
    }
    for (int i = 1000; i >= 0; --i)
    {
        for (int j = 1; j <= book[i]; ++j)
        {
            std::cout << i << ' ';
        }
    }
    std::cout << std::endl;
    return 0;
}