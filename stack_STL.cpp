#include <iostream>
#include <stack>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	stack<int> S;
	int n;
	cin >> n;

	while (n--) { // n번 반복
		string c;
		cin >> c;
		if (c == "push") {
			int t;
			cin >> t;
			S.push(t);
		}
		else if (c == "pop") {
			if (S.empty())
				cout << -1 << '\n';
			else {
				cout << S.top() << '\n';
				S.pop();
			}
		}
		else if (c == "size") {
			cout << S.size() << '\n';
		}
		else if (c == "empty") {
			cout << (int)S.empty() << '\n';
		}
		else { // top
			if (S.empty())
				cout << -1 << '\n';
			else
				cout << S.top() << '\n';
		}
	}
}