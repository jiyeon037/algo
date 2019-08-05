#include <iostream>
#include <string>

using namespace std;

int main() {
	int N, len;
	char c;
	string str[50];
	cin >> N; // 명령 개수

	for (int i = 0; i < N; i++) // 명령들 입력
		cin >> str[i];

	for (int i = 0; i < str[0].length(); i++) {
		c = str[0].at(i);
		for (int j = 0; j < N; j++) {
			if (c != str[j].at(i)) {
				cout << '?';
				break;
			}
			else if (j == N - 1) {
				cout << c;
			}
		}
	}
}