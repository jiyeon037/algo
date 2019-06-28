#include <iostream>
#include <string>
using namespace std;

int Q[1000007];
int head, tail;

void push(int val) {
	Q[tail++] = val;
}

void pop() {
	head++;
}

int front() {
	return Q[head];
}

int back() {
	return Q[tail - 1];
}

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;
	while (n--) {
		string q;
		cin >> q;
		if (q == "push") {
			int val;
			cin >> val;
			push(val);
		}
		else if (q == "pop") {
			if (head == tail) cout << -1 << '\n';
			else {
				cout << front() << '\n';
				pop();
			}
		}
		else if (q == "size") {
			cout << tail - head << '\n';
		}
		else if (q == "empty") {
			cout << (tail == head) << '\n';
		}
		else if (q == "front") {
			if (head == tail) cout << -1 << '\n';
			else cout << front() << '\n';
		}
		else { // back
			if (head == tail) cout << -1 << '\n';
			else cout << back() << '\n';
		}
	}
}