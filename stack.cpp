#include <iostream>
#include <string>
using namespace std;

const int MX = 9999999;
int arr[MX];
int cur;

void push(int val) {
	arr[cur++] = val;
}

void pop() {
	cur--;
}

int top() {
	return arr[cur - 1];
}

int main() {
	int n;
	cin >> n;

	while (n--) { // n번 반복
		string c;
		cin >> c;
		if (c == "push") {
			int t;
			cin >> t;
			push(t);
		}
		else if (c == "pop") {
			if (cur == 0)
				cout << -1 << '\n';
			else {
				cout << top() << '\n';
				pop();
			}
		}
		else if (c == "size") {
			cout << cur << '\n';
		}
		else if (c == "empty") {
			cout << (int)(cur == 0) << '\n';
		}
		else { // top
			if (cur == 0)
				cout << -1 << '\n';
			else
				cout << top() << '\n';
		}
	}
}