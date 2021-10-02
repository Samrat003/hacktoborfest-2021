#include <iostream>

using namespace std;

// function to convert decimal to binary
void decToBinary(int n)
{
	int binaryNum[32];
	int i = 0, d = n;

	while (n > 0) {
		binaryNum[i] = n % 2;
		n = n / 2;
		i++;
	}

    cout << "Binary of " << d << " = ";
	for (int j = i - 1; j >= 0; j--)
		cout << binaryNum[j];
    cout << endl;
}

int main()
{
	int n = 10;
	decToBinary(n);
	return 0;
}
