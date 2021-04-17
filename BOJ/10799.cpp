#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int result = 0;
	stack<char> S;
	string query;
	cin >> query;

	for (int i = 0; i < query.size(); i++) { // string을 돌 동안
		if (query[i] == '(')
			S.push(query[i]);
		else {
			S.pop();
			if (query[i - 1] == '(') // 레이저일 경우
				result += S.size();
			else // 직전 막대의 끝일 경우
				result += 1;
		}
	}
	cout << result << '\n';
}