#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> arr;
bool visit[10] = { 0 };

void DFS(int n) {
	if (n == M) {
		for (int i = 0; i < M; i++) {
			cout << arr[i] + 1 << ' ';
		}
		cout << '\n';
		return;
	}
	for (int i = 0; i < N; i++) {
		if (!visit[i]) {
			visit[i] = true;
			arr.push_back(i);
			visit[i] = false;
			DFS(n + 1);
			arr.pop_back();
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	DFS(0);
}