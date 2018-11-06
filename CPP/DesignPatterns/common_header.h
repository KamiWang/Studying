#include <iostream>
#include <string>
#include <vector>
#include <memory>

class IFood
{
public:
	virtual std::string GetName() = 0;
	virtual ~IFood() = default;
};

class Apple : public IFood
{
public:
	virtual std::string GetName() override
	{
		return "Apple";
	}
};

class Banana : public IFood
{
public:
	virtual std::string GetName() override
	{
		return "Banana";
	}
};

class Orange : public IFood
{
public:
	virtual std::string GetName() override
	{
		return "Orange";
	}
};

class IJuice
{
public:
	virtual std::string GetName() = 0;
	virtual ~IJuice() = default;
};

class AppleJuice : public IJuice
{
public:
	virtual std::string GetName() override
	{
		return "AppleJuice";
	}
};

class BananaJuice : public IJuice
{
public:
	virtual std::string GetName() override
	{
		return "BananaJuice";
	}
};

class OrangeJuice : public IJuice
{
public:
	virtual std::string GetName() override
	{
		return "OrangeJuice";
	}
};
