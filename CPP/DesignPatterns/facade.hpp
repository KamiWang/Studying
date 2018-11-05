#include "common_header.h"

class Facade
{
public:
	void ShowAllFruit()
	{
		std::cout << apple->GetName() << std::endl;
		std::cout << banana->GetName() << std::endl;
		std::cout << orange->GetName() << std::endl;
	}

private:
	std::unique_ptr<Apple> apple{ std::make_unique<Apple>() };
	std::unique_ptr<Banana> banana{ std::make_unique<Banana>() };
	std::unique_ptr<Orange> orange{ std::make_unique<Orange>() };
};


void Test()
{
	Facade facade;
	facade.ShowAllFruit();
}