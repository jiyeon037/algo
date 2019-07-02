#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
int cnt = 0;
vector<int> arr;

void DFS(int n) {
	if (n == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i] + 1 << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = cnt; i < N; i++) {

		arr.push_back(i);
		cnt = i;
		DFS(n + 1);
		arr.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	DFS(0);
}