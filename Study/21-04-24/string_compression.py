def solution(s):
    answer = len(s)
    step = 1 # 최대는 string의 반까지 가능

    while step <= len(s)//2: # step이 문자열의 반 이하일 동안
        cnt = 0
        now = 0 # 현재 위치
        prev = "" # 이전 값 저장
        compressed = ""
        comp_num = 1

        # 한 step일 때 뭔가 문자열을 계속 더 보니까 반복을 더 해야할거같다
        while True:

            if step*cnt >= len(s):  # 다음 반복 불가능
                break

            cnt += 1
            prev = s[now:now+step]
            now += step

            if prev == s[now:now+step]:
                comp_num += 1
            else:
                if comp_num >= 2:
                    compressed += str(comp_num) + prev
                    comp_num = 1
                else:
                    compressed += prev
        
        #print(compressed)
        if len(compressed) < answer:
            answer = len(compressed)

        step += 1
            
    return answer

s = "abcabcdede"
print(solution(s))