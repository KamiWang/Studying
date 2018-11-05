#include <iostream>
#include <string>
#include <vector>

class Food
{
public:
	virtual std::string GetName() = 0;
	virtual ~Food() = default;
};

class Apple : public Food
{
public:
	virtual std::string GetName() override
	{
		return "Apple";
	}
};

class Banana : public Food
{
public:
	virtual std::string GetName() override
	{
		return "Banana";
	}
};

class Orange : public Food
{
public:
	virtual std::string GetName() override
	{
		return "Orange";
	}
};

class Juice
{
public:
	virtual std::string GetName() = 0;
	virtual ~Juice() = default;
};

class AppleJuice : public Juice
{
public:
	virtual std::string GetName() override
	{
		return "AppleJuice";
	}
};

class BananaJuice : public Juice
{
public:
	virtual std::string GetName() override
	{
		return "BananaJuice";
	}
};

class OrangeJuice : public Juice
{
public:
	virtual std::string GetName() override
	{
		return "OrangeJuice";
	}
};
