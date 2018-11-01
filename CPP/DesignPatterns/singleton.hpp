#include <iostream>

class Singleton
{
  public:
	static std::shared_ptr<Singleton> Instance()
	{
		if (!Singleton::instance)
			Singleton::instance = std::shared_ptr<Singleton>(new Singleton);
		return Singleton::instance;
	}

	void PrintCount()
	{
		std::cout << this->count << std::endl;
	}

  private:
	Singleton()
	{
		this->count++;
	}
	Singleton &operator=(const Singleton &) = delete;
	Singleton(const Singleton &) = delete;

	static std::shared_ptr<Singleton> instance;
	int count{0};
};

std::shared_ptr<Singleton> Singleton::instance{nullptr};

void Test()
{
	Singleton::Instance()->PrintCount();
	Singleton::Instance()->PrintCount();
	Singleton::Instance()->PrintCount();
}