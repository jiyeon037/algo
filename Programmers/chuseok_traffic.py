def solution(lines):
    times = []
    for line in lines:
        date, time, during = line.split()
        time = time.split(':')
        
        end_time = int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])
        start_time = end_time - float(during[:-1]) + 0.001
        start_time = round(start_time, 3)
        print(start_time)
        times.append([start_time, end_time])

    max_ans = 0
    for time in times:
        for t in time:
            for dt in -1, 1:
                start, end = list(sorted([t, t+dt]))
                ans = 0
                for s, e in times:
                    if start <= e and s < end:
                        ans += 1
                max_ans = max(max_ans, ans)

    return max_ans

s = ["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]
print(solution(s))