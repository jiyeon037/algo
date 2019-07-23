#include <bits/stdc++.h>
// #include <set>
// #include <muntiset>
using namespace std;
int main() {
	set<int> S;
	S.insert(3); // S = {3}
	S.insert({ 5,1,7 }); // S = {1,3,5,7}
	if (S.find(6) == S.end())
		cout << "6 not in S\n";
	else
		cout << "6 in S\n";
	cout << S.size() << '\n';
	S.erase(2); // 아무 일도 일어나지 않음
	S.erase(1); // S = {3,5,7}
	S.insert(3); // set은 중복원소가 허용되지 않으므로 S = {3,5,7}
	for (auto e : S)
		cout << e << ' '; // 3 5 7
	cout << '\n';
	S.clear();
	cout << S.size() << '\n'; // 0

	multiset<int> MS;
	MS.insert(1);
	MS.insert(1);
	MS.insert(1);
	cout << MS.count(1) << '\n'; // 3
	for (auto e : MS)
		cout << e << ' '; // 1 1 1
}