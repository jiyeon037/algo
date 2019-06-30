#include <iostream>
#include <algorithm>
using namespace std;

void hanoi(int n, int from, int tmp, int to){
	if (n == 1) {
		cout << from << ' ' << to << '\n';
		return;
	}
	hanoi(n - 1, from, to, tmp); // n-1개 원반을 from에서 tmp로 이동
	cout << from << ' ' << to << "\n";
	hanoi(n - 1, tmp, from, to); // n-1개 원반을 tmp에서 to로 이동
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	cout << (1 << n) - 1 << '\n';
	hanoi(n,1,2,3);
}