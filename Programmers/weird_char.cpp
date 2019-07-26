#include <bits/stdc++.h>
using namespace std;

string solution(string s) {
	string answer = "";
	bool flag = true;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == ' ') {
			answer += " ";
			flag = true; // 0.. 첫글자
		}
		else {
			if (flag) { // 0, 대문자
				answer += toupper(s[i]);
				flag = false;
			}
			else { // 1, 소문자
				answer += tolower(s[i]);
				flag = true;
			}
		}
	}
	return answer;
}

int main() {
	string s = " wewd A SDF WEWFsdsfewSsEDD";
	cout << solution(s) << endl;
}