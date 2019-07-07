#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n, k;
	stack <pair<int, int>> S;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> k;
		while (!S.empty()) {
			if (S.top().second > k) {
				cout << S.top().first << " ";
				break;
			}
			else
			S.pop();
		}
		if (S.empty()) cout << 0 << " ";
		S.push(make_pair(i+1, k));
	}
}