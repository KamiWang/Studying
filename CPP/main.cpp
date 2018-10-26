#include "DesignPatterns/header.h"

namespace A::B::C {
	int a;
}


int main()
{
	auto s = [](auto x, auto y) {return x + y; };
	
	std::cout<< s(1, 1);

	int* c = new int{ 10 };

	std::cout << *c;

	Print();
    std::cin.get();
    return 0;
}