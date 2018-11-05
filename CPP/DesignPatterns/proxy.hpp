#include "common_header.h"

class IProxy : public IFood
{
public:
	IProxy(std::unique_ptr<IFood> food)
	{
		this->food = std::move(food);
	}

	virtual std::string GetName() override
	{
		return food->GetName();
	}

protected:
	std::unique_ptr<IFood> food;
};


class ProxyApple : public IProxy
{
public:
	ProxyApple(std::unique_ptr<Apple> apple) : IProxy(std::move(apple)) {}

	void EatApple()
	{
		std::cout << "Ready to Eat" << std::endl;
		std::cout << "eat" << this->food->GetName() << std::endl;
		std::cout << "byebye" << std::endl;
	}
};

class ProxyBanana : public IProxy
{
public:
	ProxyBanana(std::unique_ptr<Banana> banana) : IProxy(std::move(banana)) {}

	void EatBanana()
	{
		std::cout << "Ready to Eat" << std::endl;
		std::cout << "eat" << this->food->GetName() << std::endl;
		std::cout << "byebye" << std::endl;
	}
};


void Test()
{
	ProxyApple apple(std::make_unique<Apple>());
	apple.EatApple();
	ProxyBanana banana(std::make_unique<Banana>());
	banana.EatBanana();
}