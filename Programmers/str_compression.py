def solution(s):
    answer = len(s)

    for now in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:now]

        count = 1
        for j in range(now, len(s), now):
            if prev == s[j:j+now]:
                count += 1
            else:
                if count >= 2:
                    compressed += str(count) + prev
                else:
                    compressed += prev

                prev = s[j:j+now]
                count = 1

        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed))
    return answer

s = "abcabcdede"
print(solution(s))