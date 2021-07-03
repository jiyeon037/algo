# 탈락 경우
# 1. 했던 단어 또 하기
# 2. 안 이어지는 단어 말하기

def get_fail_answer(n, idx):
    idx += 1

    if idx % n == 0:
        first = n
        second = idx // n
    else:
        first = idx % n
        second = idx // n + 1

    return [first, second]

def solution(n, words):
    tried = []
    idx = 0
    fail_flag = False

    while not fail_flag and idx < len(words)-1:

        tried.append(words[idx])
        idx += 1

        if words[idx][0] == tried[-1][-1]:

            if words[idx] in tried:
                fail_flag = True
            else:
                print("성공 ", idx)
        else:
            fail_flag = True

    if fail_flag:
        return get_fail_answer(n, idx)

    return [0,0]

#print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
#print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))