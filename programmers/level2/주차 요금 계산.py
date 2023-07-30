import math
def solution(fees, records):
    global fee
    answer = []
    parking_lot = []
    cal = []
    basic_time = fees[0]
    basic_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    for record in records:
        t, num, flag = record.split(' ')[0], record.split(' ')[1], record.split(' ')[2]
        hour, minute = map(int, t.split(':'))
        for info in parking_lot:
            if num in info:
                car = num
                first_hour, first_minute = map(int, info[0].split(':'))
                parking_lot.remove(info)
                if minute < first_minute:
                    minute += 60
                    hour -= 1
                used_time = 60 * (hour - first_hour) + (minute - first_minute)

                cal.append([car, used_time])
        # parking lot에 없는 경우
        if flag == "IN":
            parking_lot.append([t, num])
    for car in parking_lot:
        first_hour, first_minute = map(int, car[0].split(':'))
        used_time = (23 - first_hour) * 60 + (59-first_minute)
        cal.append([car[1], used_time])
    result_dict = {}
    for key, value in cal:
        if key in result_dict:
            result_dict[key] += value
        else:
            result_dict[key] = value

    result_list = sorted([[key, value] for key, value in result_dict.items()], key = lambda x:x[0])
    for arr in result_list:
        print(arr)
        if arr[1] <= basic_time:
            answer.append(basic_fee)
        elif arr[1] > basic_time:
            answer.append(basic_fee + math.ceil((arr[1] - basic_time) / unit_time) * unit_fee)

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
