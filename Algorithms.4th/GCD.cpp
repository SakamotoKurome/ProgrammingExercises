#include <iostream>

class GCD
{
public:
    static int gcd(int p, int q)
    {
        if (q == 0)
        {
            return p;
        }
        int r = p % q;
        return gcd(q, r);
    }
};

int main()
{
    std::cout << GCD::gcd(12, 15) << std::endl;
    return 0;
}