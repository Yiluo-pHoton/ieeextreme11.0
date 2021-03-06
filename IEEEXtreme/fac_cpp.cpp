#include <iostream>

using namespace std;

long int facFromTo(int b, int c);
long int fac(int a);
long int power(int base, long int exp);

int main() {
	int n;
	cin >> n;

	int a, b, c;
	for (int i = 0; i < n; i++) {
		cin >> a >> b >> c;
		if (a == 1) 
			cout << 1;
		else
			cout << power(a, facFromTo(b, c) / fac(b - c)) % (power(10, 9) + 7) << endl;
	}
	return 0;	
}
long int facFromTo(int b, int c) {
	long int prod(1);
	for (int i = b; i > c; i--) {
		prod *= i;
	}
	return prod;
}

long int fac(int a) {
	long int prod(1);
	for (int i = 1; i < a + 1; i++) {
		prod *= i;
	}
	return prod;
}

long int power(int base, long int exp) {
	if (exp == 0) return 1;
	else if (exp == 1) return base;
	else if (exp % 2 == 0) 
		return power(base, exp/2) * power(base, exp/2);
	else 
		return base * power(base, exp/2) * power(base, exp/2);
}

