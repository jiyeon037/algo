#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(int num) {
	int answer = 0;

	for(int cnt = 0; cnt <= 450; cnt++) {

		if (num == 1) {
			return cnt;
		}

		num % 2 == 0 ? num = num / 2: num = num * 3 + 1;

	}
	return -1;
}

int main() {
	int num;
	cin >> num;
	cout << solution(num) << endl;
}