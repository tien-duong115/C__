// power1.cpp

#include <iostream>

int power(int m, int n)
{
    int r = 1;
    for (int i = 1; i<= n; ++i) r *= m;
    return r;
}

template<int m, int n>
struct Power{
    static int const value = m * Power<m,n-1>::value;
};

template<int m>
struct Power<m,0>{
   static int const value = 1;
};


template<int i, int o>
struct  recursive
    {
        static int const value = i + recursive<i, o - 1>::value;
    };

template<int i>
struct  recursive<i, 0>
{
    static int const value = 1;
};

1 + 2+ 3 +4 +5


int main()
{
    std::cout << power(2,10) << std::endl;
    std::cout << Power<2,10>::value << std::endl;
    std::cout << recursive<1,5>::value << std::endl;

}
