#include <iostream>

struct ConstMember
{
    const int *p; // 常类型指针成员
    int *const q; // 常指针变量成员
    int s;
    void func()
    {
        std::cout << "General Function" << std::endl;
    }
    void constFunc1() const
    {
        std::cout << "Const Function 1" << std::endl;
    }
    void constFunc2(int ss) const
    {
        // func(); // 常成员函数不能调用普通成员函数
        constFunc1(); // 常成员函数可以调用常成员函数
        // s = ss; // 常成员函数不能改变普通成员变量
        // p = &ss; // 常成员函数不能改变常成员变量
    }
};

int main()
{
    const int a = 1;
    int b = 1;
    struct ConstMember c = {.p = &a, .q = &b};
    // *(c.p) = 2; // 常类型指针无法改变指向的值
    c.p = &b;   // 常类型指针可以改变指针指向
    *(c.q) = 2; // 常指针变量可以改变指向的值
    // c.q = &a; // 常指针变量无法改变指针指向
    const struct ConstMember d = c;
    // d.func(); // 常对象不能调用普通成员函数
    d.constFunc2(b); // 常对象可以调用常成员函数
    return 0;
}