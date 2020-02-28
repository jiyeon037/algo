curList = []
nextList = []
mapList = [[50,45,37,32,30],
        [35,50,40,20,25],
        [30,30,25,17,28],
        [27,24,22,15,10]]

# 상하좌우
dirX = [0,0,-1,1]
dirY = [1,-1,0,0]

cnt = 0

# 초기위치 지정
curX = 0
curY = 0
curSpot = mapList[curX][curY]
curList.append(curSpot)

while(True):
    if curList is None: # list가 비어있으면 반복 종료
        break

    for curSpot in curList:

        for i in range(4): # 상하좌우 검사

            if curSpot == mapList[3][4]: # 리스트에 검출이 끝난 값이 있으면
                cnt += 1 # 카운트를 업하고
                curList.remove(curSpot) # 리스트에서 해당 값을 지운다
                continue

            curX += dirX[i]
            curY += dirY[i]

            if curX < 0 or curX >= 4 or curY < 0 or curY >= 5:
                continue

            nextSpot = mapList[curX][curY]

            if curSpot > nextSpot:
                nextList.append(nextSpot)

    curList = nextList

print(cnt)