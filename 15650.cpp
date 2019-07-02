#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
int cnt;
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

	// 중복을 허용하지 않는다 -> {1,2}와 {2,1}을 하나로 본다
	// => 다음 출력 수 > 이전 출력 수 
	for (int i = cnt; i < N; i++) {
		if (!visit[i]) {
			visit[i] = true;
			arr.push_back(i);
			cnt = i;
			DFS(n + 1);
			arr.pop_back();
			visit[i] = false;
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N >> M;
	DFS(0);
}