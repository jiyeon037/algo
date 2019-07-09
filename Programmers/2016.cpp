#include <string>

using namespace std;

string solution(int a, int b) {
	string answer = "";
	string arr[7] = { "THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED" };

	int day = b;
	for (int i = 1; i < a; i++) {
		switch (i) {
		case 4:
		case 6:
		case 9:
		case 11:
			day += 30;
			break;
		case 2:
			day += 29;
			break;
		default:
			day += 31;
			break;
		}
	}
	day %= 7;
	answer = arr[day];

	return answer;
}