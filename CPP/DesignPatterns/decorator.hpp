#include "common_header.h"

class DecoratorFood : public Food
{
public:
	DecoratorFood(std::unique_ptr<Food> food)
	{
		this->food = std::move(food);
	}

	virtual ~DecoratorFood() = default;

	virtual std::string GetName() override
	{
		return food->GetName();
	}

	virtual void PrintName()
	{
		std::cout << this->GetName() << std::endl;
	}

	virtual void ShowColor() = 0;

protected:
	std::unique_ptr<Food> food;
};

class DecoratorApple : public DecoratorFood
{
public:
	DecoratorApple(std::unique_ptr<Apple> apple) : DecoratorFood(std::move(apple)) {}

	virtual void ShowColor() override
	{
		std::cout << "It is Red" << std::endl;
	}
};

class DecoratorBanana : public DecoratorFood
{
public:
	DecoratorBanana(std::unique_ptr<Banana> banana) : DecoratorFood(std::move(banana)) {}

	virtual void ShowColor() override
	{
		std::cout << "It is Yellow" << std::endl;
	}
};

void Test()
{
	DecoratorApple apple(std::make_unique<Apple>());
	DecoratorBanana banana(std::make_unique<Banana>());

	apple.PrintName();
	apple.ShowColor();
	banana.PrintName();
	banana.ShowColor();
}