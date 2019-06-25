#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>
using namespace std;
#define X first
#define Y second // pair에서 first, second를 줄여쓰기 위해서 사용

// 다차원 배열에서 어떤 칸과 연결된 영역을 찾는 알고리즘 (Flood Fill)
int board[502][502] = 
{{1,1,1,0,1,0,0,0,0,0},
{1,0,0,0,1,0,0,0,0,0},
{1,1,1,0,1,0,0,0,0,0},
{1,1,0,0,1,0,0,0,0,0},
{0,0,0,0,0,0,0,0,0,0},
{0,0,0,0,0,0,0,0,0,0}}; // 1이 파란 칸, 0이 빨간 칸에 대응
bool vis[502][502]; // 해당 칸을 방문했는지 여부를 저장
int n=7, m=10; // n = 행의 수, m = 열의 수
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1}; // 상하좌우 네 방향을 의미

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0); // c++ 입출력 객체 가속
    queue<pair<int,int>> Q;
    vis[0][0]=1; // (0,0)을 방문했다고 명시
    Q.push({0,0}); // 큐에 시작점인 (0,0)을 삽입
    while(!Q.empty()){
        auto cur = Q.front();
        Q.pop();
        cout<<'('<<cur.X<<", "<<cur.Y<< ") -> ";
        for(int dir=0; dir<4; dir++){ // 상하좌우 순서로 인접한 좌표 검사
        int nx = cur.X + dx[dir];
        int ny = cur.Y + dy[dir]; // nx, ny에 dir에서 정한 방향의 인접한 칸의 좌표가 들어감
        if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue; // 범위 밖일 경우 넘어감
        if(vis[nx][ny] == 1 || board[nx][ny] != 1) continue; // 이미 방문한 칸이거나 파란 칸이 아닐 경우
        vis[nx][ny] = 1; // (nx, ny)를 방문했다고 명시
        Q.push({nx,ny});
        }
    }
}