#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	int T;
	cin >> T;

	while (T--) {
		stack<int> S;
		string query;
		cin >> query;
		for (auto c : query) {
			if (c == '(' || c == '{') S.push(c);
			else {
				if (S.empty()) {
					S.push('x');
				break;
			}
			if (c == ')') {
				if (S.top() != '(') break; // 스택이 top과 대응되지 않는 괄호라면 강제로 탈출
			}
			else {
				if (S.top() != '{') break;
			}
			S.pop();
		}
		}
		if (S.empty()) cout << "YES\n";
		else cout << "NO\n";
	}
}