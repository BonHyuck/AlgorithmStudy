def solution(lines):
    answer = 0
    arr = []
    for l in lines:
        date, time, duration = l.split()
        real_time = time.split(':')
        hour = int(real_time[0]) * 3600 * 1000
        minute = int(real_time[1]) * 60 * 1000
        second = int(real_time[2].split('.')[0]) * 1000 + int(real_time[2].split(".")[1])
        duration = duration[:-1]
        final_duration = int(duration.split('.')[0]) * 1000 + int(duration.split('.')[1] if len(duration) > 1 else 0)
        end_time = hour + minute + second
        start_time = end_time - final_duration + 1

        arr.append([start_time, end_time])

    for start, end in arr:
        cnt = 0
        for compare_start, compare_end in arr:
            if compare_start < start + 1000 and compare_end >= start:
                cnt += 1
        answer = max(cnt, answer)

        cnt = 0
        for compare_start, compare_end in arr:
            if compare_start < end + 1000 and compare_end >= end:
                cnt += 1
        answer = max(cnt, answer)

    return answer

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))
