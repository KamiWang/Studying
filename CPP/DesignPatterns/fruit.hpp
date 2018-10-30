class Fruit
{
public:
	virtual std::string GetName() = 0;
};

class Apple : public Fruit
{
public:
	virtual  std::string GetName() override
	{
		return "苹果";
	}
};

class Banana : public Fruit
{
public:
	virtual  std::string GetName() override
	{
		return "香蕉";
	}
};

class Orange : public Fruit {
public:
	virtual  std::string GetName() override
	{
		return "桔子";
	}
};
