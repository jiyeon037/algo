#include <iostream>
#include <string>

using namespace std;

int solution(string str) {

	return stoi(str);
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	string str;
	cin >> str;

	cout << solution(str) << endl;
}