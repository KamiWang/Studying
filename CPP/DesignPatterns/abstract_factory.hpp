#include <iostream>
#include <string>
#include <vector>
#include "food.hpp"

class AbstractFactory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() = 0;
	virtual std::shared_ptr<Juice> MakeJuice() = 0;
};

class AppleFactory : public AbstractFactory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Apple>();
	}

	virtual std::shared_ptr<Juice> MakeJuice() override
	{
		return std::make_shared<AppleJuice>();
	}
};

class BananaFactory : public AbstractFactory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Banana>();
	}

	virtual std::shared_ptr<Juice> MakeJuice() override
	{
		return std::make_shared<BananaJuice>();
	}
};

class OrangeFactory : public AbstractFactory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Orange>();
	}

	virtual std::shared_ptr<Juice> MakeJuice() override
	{
		return std::make_shared<OrangeJuice>();
	}
};


void Test()
{
	AppleFactory apple_factory;
	BananaFactory banana_factory;
	OrangeFactory orange_factory;

	std::vector<std::shared_ptr<Food>> all_fruits;
	all_fruits.emplace_back(apple_factory.MakeFruit());
	all_fruits.emplace_back(banana_factory.MakeFruit());
	all_fruits.emplace_back(orange_factory.MakeFruit());
	for (const auto& it : all_fruits)
		if (it) std::cout << it->GetName() << std::endl;

	std::vector<std::shared_ptr<Juice>> all_juice;
	all_juice.emplace_back(apple_factory.MakeJuice());
	all_juice.emplace_back(banana_factory.MakeJuice());
	all_juice.emplace_back(orange_factory.MakeJuice());
	for (const auto& it : all_juice)
		if (it) std::cout << it->GetName() << std::endl;
}