#include <iostream>
#include <string>
#include <vector>

using namespace std;

int collatz(int num) {
	static int cnt = 0;
	if (num == 1) return cnt;

	if (num % 2 == 0) {
		cnt++;
		collatz(num / 2);
	}
	else {
		cnt++;
		collatz(num * 3 + 1);
	}
}

int main() {
	int num, res;
	cin >> num;

	res = collatz(num);
	cout << res << endl;
}