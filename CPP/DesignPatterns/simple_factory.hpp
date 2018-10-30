//简单工厂模式

#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include "fruit.hpp"


class FruitSimpleFactory
{
public:
	enum class FruitType
	{
		APPLE,
		BANANA,
		ORANGE
	};

	static std::shared_ptr<Fruit> NewFruit(FruitType type)
	{
		switch (type)
		{
		case FruitType::APPLE:
			return std::make_shared<Apple>();
		case FruitType::BANANA:
			return std::make_shared<Banana>();
		case FruitType::ORANGE:
			return std::make_shared<Orange>();
		default:
			return nullptr;
		}
	}
};

void TestSimpleFactory()
{
	auto apple = FruitSimpleFactory::NewFruit(FruitSimpleFactory::FruitType::APPLE);
	auto banana = FruitSimpleFactory::NewFruit(FruitSimpleFactory::FruitType::BANANA);
	auto orange = FruitSimpleFactory::NewFruit(FruitSimpleFactory::FruitType::ORANGE);

	std::vector<std::shared_ptr<Fruit>> all_fruits{ apple,banana,orange };

	for (const auto& it : all_fruits)
		std::cout << it->GetName() << std::endl;
}