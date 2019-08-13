#include <bits/stdc++.h>
using namespace std;

int s[1000][3];
int d[1000][3];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;

	// N개의 줄에 각각 RGB 비용 입력
	for (int i = 0; i < n; i++)
		cin >> s[i][0] >> s[i][1] >> s[i][2];

	d[0][0] = s[0][0];
	d[0][1] = s[0][1];
	d[0][2] = s[0][2];

	// 모든 가능한 RGB를 메모한다
	for (int i = 1; i < n; i++) { // 0=R, 1=G, 2=B
		d[i][0] = min(d[i - 1][1], d[i - 1][2]) + s[i][0];
		d[i][1] = min(d[i - 1][0], d[i - 1][2]) + s[i][1];
		d[i][2] = min(d[i - 1][0], d[i - 1][1]) + s[i][2];
	}

	cout << min(min(d[n - 1][0], d[n - 1][1]), d[n - 1][2]);

}