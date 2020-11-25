def solution(lines):
    max_ans = 0
    times = []
    for line in lines:
        date, time, during = line.split()
        time = time.split(':')
        end_time = int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])
        start_time = end_time - float(during[:-1]) + 0.001
        start_time = round(start_time, 3)
        times.append([start_time, end_time])

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