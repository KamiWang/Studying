#include "common_header.h"

class IFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() = 0;
	virtual ~IFactory() = default;
};

class AppleFactory : IFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Apple>();
	}
};

class BananaFactory : IFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Banana>();
	}
};

class OrangeFactory : IFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Orange>();
	}
};

void Test()
{
	AppleFactory apple_factory;
	BananaFactory banana_factory;
	OrangeFactory orange_factory;
	std::vector<std::shared_ptr<IFood>> all_fruits;
	all_fruits.emplace_back(apple_factory.MakeFruit());
	all_fruits.emplace_back(banana_factory.MakeFruit());
	all_fruits.emplace_back(orange_factory.MakeFruit());
	for (const auto &it : all_fruits)
		if (it)
			std::cout << it->GetName() << std::endl;
}