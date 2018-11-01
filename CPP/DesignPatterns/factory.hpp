#include <iostream>
#include <string>
#include <vector>
#include "food.hpp"

class Factory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() = 0;
	virtual ~Factory() = default;
};

class AppleFactory : Factory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Apple>();
	}
};

class BananaFactory : Factory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Banana>();
	}
};

class OrangeFactory : Factory
{
public:
	virtual std::shared_ptr<Food> MakeFruit() override
	{
		return std::make_shared<Orange>();
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
	for (const auto &it : all_fruits)
		if (it)
			std::cout << it->GetName() << std::endl;
}