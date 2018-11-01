#include <iostream>
#include <string>
#include <vector>
#include "food.hpp"

class SimpleFactory
{
  public:
	enum class FruitType
	{
		APPLE,
		BANANA,
		ORANGE
	};

	static std::shared_ptr<Food> NewFruit(FruitType type)
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

void Test()
{
	auto apple = SimpleFactory::NewFruit(SimpleFactory::FruitType::APPLE);
	auto banana = SimpleFactory::NewFruit(SimpleFactory::FruitType::BANANA);
	auto orange = SimpleFactory::NewFruit(SimpleFactory::FruitType::ORANGE);
	std::vector<std::shared_ptr<Food>> all_fruits{apple, banana, orange};
	for (const auto &it : all_fruits)
		if (it)
			std::cout << it->GetName() << std::endl;
}