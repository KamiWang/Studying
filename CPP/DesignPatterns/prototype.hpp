#include "common_header.h"

class Prototype
{
public:
	int a{ 1 };
	int* b{ new int{2} };
	std::string c{ " HelloWorld! " };

	Prototype() = default;
	Prototype(const Prototype& src) = delete;
	const Prototype& operator=(const Prototype& src) = delete;

	std::shared_ptr<Prototype> Clone() {
		auto ptr = std::make_shared<Prototype>();
		ptr->a = this->a;
		delete ptr->b;
		ptr->b = new int{ *(this->b) };
		ptr->c = this->c;
		return ptr;
	}

	~Prototype() {
		delete b;
	}
};

void Test()
{
	auto pt1 = std::make_shared<Prototype>();
	auto pt2 = pt1->Clone();

	*(pt2->b) = 999;
	pt2->c = " NoHello! ";

	std::cout << pt1->a << pt1->c << *pt1->b << std::endl;
	std::cout << pt2->a << pt2->c << *pt2->b << std::endl;
}