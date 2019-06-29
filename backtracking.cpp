#include <iostream>
#include <vector>
using namespace std;

int n, m;

void func(vector<int> arr, vector<bool> isused, int k) { // 현재까지 k개까지 수를 택했음
	if (k == m) { // m개를 모두 택했으면
		for (int i = 0; i < m; i++) // arr에 기록해둔 수들을 출력
			cout << arr[i] + 1 << ' ';
		cout<<'\n';
		return;
	}

	for (int i = 0; i < n; i++) { // 1부터 n까지의 수에 대해
		if (!isused[i]) { // 아직 i가 사용되지 않았으면
			arr[k] = i; // k번째 수를 i로 저장
			isused[i] = 1; // i를 사용되었다고 표시
			func(arr, isused, k + 1); // 다음 수를 정하러 한단계 더 들어감
			isused[i] = 0; // k번째 수를 i로 정한 경우에 대해 다 확인했으니 i를 이제 사용되지 않았다고 명시
		}
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> n >> m;
	vector<int> arr(m);
	vector<bool> isused(n);
	func(arr, isused, 0);
}