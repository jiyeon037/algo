def solution(s):
    zero_count = 0
    convert_bin = 0

    while s != '1':
        for i in range(len(s)):
            if s[i] == '0':
                zero_count += 1
        s = s.replace('0', '')
        
        s = bin(len(s))[2:]
        convert_bin += 1

    return [convert_bin, zero_count]

print(solution("01110"))