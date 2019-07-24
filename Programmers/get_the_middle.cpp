#include <string>

using namespace std;

string solution(string s) {
    string answer = "";
    int length = s.length();
    if(length%2 == 1){
        answer = s[length/2];
    }
    else{
        answer = s[length/2 - 1];
        answer += s[length/2];
    }
    return answer;
}