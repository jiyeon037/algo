#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
	sort(participant.begin(), participant.end());
	sort(completion.begin(), completion.end());
	for (int i = 0; i < completion.size(); i++) {
		if (participant[i] != completion[i]) {
		
			return participant[i];
		}
	}
	return participant.back();
}

int main() {
	vector<string> par;
	vector<string> com;
	par.push_back("leo");
	par.push_back("kiki");
	par.push_back("eden");
	com.push_back("eden");
	com.push_back("kiki");
	cout << solution(par, com) << endl;
    
}