#include <iostream>

using namespace std;

// Function to convert binary to decimal
int binaryToDecimal(int n)
{
	int num = n;
	int dec_value = 0;
	int base = 1;
	int temp = num;

	while (temp) {
		int last_digit = temp % 10;
		temp = temp / 10;
		dec_value += last_digit * base;
		base = base * 2;
	}

	return dec_value;
}

int main()
{
	int num = 10101001;
	cout << "Decimal of " << num << " = " << binaryToDecimal(num) << endl;
    return 0;
}
