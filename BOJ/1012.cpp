#include <iostream>
#include <queue>
#define MAX_SIZE 51

using namespace std;
void BFS(int x, int y);

int cabage[MAX_SIZE][MAX_SIZE] = { 0, }; // 영역
int visit[MAX_SIZE][MAX_SIZE] = { 0, }; // 칸 방문 여부 저장
	int n,m,k;
	int dx[4] = { 0,0,1,-1 };
	int dy[4] = { 1,-1,0,0 }; // 상하좌우 네 방향
	queue<pair<int, int>> Q;

	int main() {
		int T;
		cin >> T;

		while (T--) {

			cin >> m >> n >> k;
			int cnt = 0;

			while (k--) {
				int x, y;
				cin >> x >> y;
				cabage[x][y] = 1;
			}

			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (cabage[i][j] == 1 && visit[i][j] == 0) {
						visit[i][j] = 1;
						cnt++;
						BFS(i, j);
					}
				}
			}

			cout << cnt << "\n";

			for (int i = 0; i < MAX_SIZE; i++) {
				for (int j = 0; j < MAX_SIZE; j++) {
					visit[i][j] = 0;
					cabage[i][j] = 0;
				}
			}
		}
		return 0;
	}


	void BFS(int x, int y) {

		Q.push({ x,y });

		while (!Q.empty()) {
			x = Q.front().first;
			y = Q.front().second;
			Q.pop();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if ((nx < 0 || nx >= MAX_SIZE || ny < 0 || ny >= MAX_SIZE) || visit[nx][ny] == 1)
					continue;
				if (cabage[nx][ny] == 1) {
					visit[nx][ny] = visit[x][y];
					Q.push({ nx,ny });
				}
			}
		}
	}