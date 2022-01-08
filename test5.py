import time
import bisect


def convert_second_time(date_str):
    return int(date_str[:2]) * 3600 + int(date_str[3:5]) * 60 + int(date_str[6:])


def solution(play_time, adv_time, logs):
    play_time = convert_second_time(play_time)
    adv_time = convert_second_time(adv_time)

    timestamps = []
    for log in logs:
        timestamps.append((convert_second_time(log[:8]), True))
        timestamps.append((convert_second_time(log[9:]), False))

    timestamps.sort(key=lambda x: x[0])

    keys = [0,]
    deltatimes = []
    start_time = 0
    count = 0
    for t, is_start in timestamps:
        if start_time != t:
            keys.append(t)
            deltatimes.append(((t - start_time) * count, count))
            start_time = t
        count += 1 if is_start else -1
    keys.append(play_time)
    deltatimes.append((0, 0))

    max_time = 0
    answer = 0
    for s, t in enumerate(keys):
        end_time = t + adv_time
        if end_time > play_time:
            break

        total_time = 0    
        e = bisect.bisect_left(keys, end_time)
        for deltatime, count in deltatimes[s:e]:
            total_time += deltatime
        total_time += count * (end_time - keys[e])
        if max_time < total_time:
            max_time = total_time
            answer = t

    return time.strftime('%H:%M:%S', time.gmtime(answer))


a = solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
print(a)
a = solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])
print(a)