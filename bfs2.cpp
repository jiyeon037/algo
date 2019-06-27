#include <iostream>
#include <utility>
#include <queue>
#include <algorithm>
using namespace std;
#define X first
#define Y second

int board[502][502]; // 1 = 파란칸, 0 = 빨간칸
bool vis[502][502]; // 칸 방문 여부 저장
int n,m;
int dx[4] = {0,0,1,-1};
int dy[4] = {1,-1,0,0}; // 상하좌우 네 방향

int main(){
    cin >> n >> m;
    for(int i=0; i<n; i++)
        for(int j=0; j<m; j++)
            cin >> board[i][j];
    
    int mx=0; // 그림의 최대값
    int num=0; // 그림의 수

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(board[i][j] == 0 || vis[i][j])
                continue;
            num++; // 그림의 수 1 증가
            queue<pair<int, int>> Q;
            vis[i][j] = 1; // bfs 시작 준비
            Q.push({i,j});
            
            int area = 0; // 그림의 넓이
            while(!Q.empty()){
                area++; // 큐에 들어있는 원소를 하나 뺄 때 마다 넓이 1씩 증가
                auto cur = Q.front();
                Q.pop();
                for(int dir=0; dir<4; dir++){
                    int nx = cur.X + dx[dir];
                    int ny = cur.Y + dy[dir];

                    if(nx < 0 || nx >= n || ny < 0|| ny >= m)
                        continue;
                    if(vis[nx][ny] || board[nx][ny] != 1)
                        continue;
                    vis[nx][ny] = 1; // 방문 명시
                    Q.push({nx,ny});
                }
            }
            mx = max(mx, area); // area가 mx보다 크면 mx에 area 대입
        }
    }
    cout << num << '\n' << mx;
}