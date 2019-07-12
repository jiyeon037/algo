#include <iostream>
#include <string>

using namespace std;

string solution(string s, int n) {
    string answer = "";
	n = n % 26;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] <= 'z' && s[i] >= 'a') {
			answer += ((s[i] + -'a' + n)%26)+'a';
		} else if (s[i] <= 'Z' && s[i] >= 'A') {
			answer += ((s[i] + n - 'A')%26)+'A';
		} 	else {
			answer += s[i];
		}
	}

    return answer;
}

int main() {
	string s;
	int n;
	getline(cin, s);
	cin >> n;
	string res = solution(s, n);
	cout << res << '\n';
}