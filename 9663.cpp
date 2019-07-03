#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int N, cnt;
int *col = new int[N];

bool isPossible(int q[], int row) {
	if (row < 1) return true; // 첫 줄은 상관 없음
	for (int i = 0; i < row; i++) { // n번째 행에서
		if (q[row] == q[i] || row - i == abs(q[row] - q[i]))
			return false;
	}
	return true;
}

void DFS(int q[], int row) {
	for (int i = 0; i < N; i++) {
		q[row] = i;
		if (isPossible(q, row)) {
			if (row == N - 1) {
				cnt++;
			}
			else {
				DFS(q, row + 1);
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> N;

	DFS(col, 0);

	cout << cnt << '\n';
}