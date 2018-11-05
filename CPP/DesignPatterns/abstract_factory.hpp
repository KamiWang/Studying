#include "common_header.h"

class IAbstractFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() = 0;
	virtual std::shared_ptr<IJuice> MakeJuice() = 0;
};

class AppleFactory : public IAbstractFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Apple>();
	}

	virtual std::shared_ptr<IJuice> MakeJuice() override
	{
		return std::make_shared<AppleJuice>();
	}
};

class BananaFactory : public IAbstractFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Banana>();
	}

	virtual std::shared_ptr<IJuice> MakeJuice() override
	{
		return std::make_shared<BananaJuice>();
	}
};

class OrangeFactory : public IAbstractFactory
{
public:
	virtual std::shared_ptr<IFood> MakeFruit() override
	{
		return std::make_shared<Orange>();
	}

	virtual std::shared_ptr<IJuice> MakeJuice() override
	{
		return std::make_shared<OrangeJuice>();
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

	std::vector<std::shared_ptr<IJuice>> all_juice;
	all_juice.emplace_back(apple_factory.MakeJuice());
	all_juice.emplace_back(banana_factory.MakeJuice());
	all_juice.emplace_back(orange_factory.MakeJuice());
	for (const auto &it : all_juice)
		if (it)
			std::cout << it->GetName() << std::endl;
}