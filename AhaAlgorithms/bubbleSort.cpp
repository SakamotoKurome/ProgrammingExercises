#include <iostream>
#include <vector>

int main()
{
    int a[100];
    int n;
    std::cin >> n;
    for (int i = 1; i <= n; ++i)
    {
        std::cin >> a[i];
    }
    int t;
    for (int i = 1; i <= n - 1; ++i)
    {
        for (int j = 1; j <= n - i; ++j)
        {
            if (a[j] < a[j + 1])
            {
                t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
        }
    }
    for (int i = 1; i <= n; i++)
    {
        std::cout << a[i] << ' ';
    }
    std::cout << std::endl;
    return 0;
}