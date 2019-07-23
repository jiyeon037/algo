#include <bits/stdc++.h>
// #include <map>
// #include <muntimap>
using namespace std;
int main() {
	map<string, int> M; // key : string, value : int
	M["kim"] = 2621672;
	M["qwrtty"] = 4271234;
	M["apple"] = -42234;
	for (auto e : M)
		cout << e.first << " : " << e.second << '\n';
	/*
	apple : -42234
	qwerty : 4271234
	kim : 2621672
	*/
	cout << M.size() << '\n'; // 2
	if (M.find("apple") == M.end())
		cout << "key apple not in M\n";
	else
		cout << "key apple in M\n"; // 출력

	M["apple"] = 1234;
	cout << M["apple"] << '\n'; // 1234
	M.erase("qwerty");
	M.clear();

	multimap<int, string> MS;
	//Multimap은 동일한 키가 여러 개일 수 있으나 [] 연산자로 원소에 접근할 수 없다.
	MS.insert({ 1,"hello" });
	MS.insert({ 1,"hi" });
	MS.insert({ -10,"zcv" });
	for (auto e : MS)
		cout << e.first << " : " << e.second << '\n';
	/*
	-10 : zcv
	1 : hello
	1 : hi
	*/

}