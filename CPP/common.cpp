
bool CheckOverflow(int a, int b)
{
	//溢出检测
	int c = a + b;

	return ((c^a) >= 0 || (c^b) >= 0);
}