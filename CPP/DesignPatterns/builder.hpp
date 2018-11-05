#include "common_header.h"

class IBuilder
{
public:
	virtual void BuildCPU() = 0;
	virtual void BuildHD() = 0;
	virtual void BuildMainBoard() = 0;
	virtual void BuildMemory() = 0;
};


class PCBuilder : public IBuilder
{
public:
	virtual void BuildCPU() override
	{
		computer.push_back("CPU installation is complete");
	}
	virtual void BuildHD() override
	{
		computer.push_back("HD installation is complete");
	}
	virtual void BuildMainBoard() override
	{
		computer.push_back("MainBoard installation is complete");
	}
	virtual void BuildMemory() override
	{
		computer.push_back("Memory installation is complete");
	}

	void Show()
	{
		for (const auto& it : computer)
			std::cout << it << std::endl;

		if (computer.size() == 4)
			std::cout << "computer is OK!!!" << std::endl;
	}
private:
	std::vector<std::string> computer;
};


class Director
{
public:
	Director(IBuilder& builder)
	{
		builder.BuildCPU();
		builder.BuildHD();
		builder.BuildMainBoard();
		builder.BuildMemory();
	}
};

void Test()
{
	PCBuilder wmj;
	Director director(wmj);
	wmj.Show();
}
