#include "common_header.h"

class Target
{
public:
	virtual void Show() = 0;
};

class Adaptee
{
public:
	Adaptee(const std::string& name)
	{
		this->name = name;
	}

	void AdvanceShow()
	{
		std::cout << "this is " << name << std::endl;
	}

private:
	std::string name;
};

class Adapter : public Target
{
public:
	Adapter(std::unique_ptr<Adaptee> ada)
	{
		adaptee = std::move(ada);
	}

	virtual void Show() override
	{
		adaptee->AdvanceShow();
	}
private:
	std::unique_ptr<Adaptee> adaptee;
};


void Test()
{
	std::shared_ptr<Target> target = std::make_shared<Adapter>(std::make_unique<Adaptee>("HelloWorld!!!"));

	target->Show();
}