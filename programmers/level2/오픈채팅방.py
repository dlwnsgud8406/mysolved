def change(id, nickname, log):
    for info in log:
        if info[0] == id:
            info[1] = nickname
def solution(record):
    answer = []
    log = []
    for command in record:
        com = command.split(' ')
        if com[0] == 'Enter':
            change(com[1], com[2], log)
            log.append([com[1], com[2], 0])
        elif com[0] == 'Change':
            change(com[1], com[2], log)
        else:
            for l in log:
                if com[1] == l[0]:
                    log.append([com[1], l[1], 1])
                    break
    for l in log:
        string = l[1]
        if l[2] == 0:
            string += '님이 들어왔습니다.'
        else:
            string += '님이 나갔습니다.'
        answer.append(string)
    return answer

# 초고속 풀이법
def solution(record):
    answer = []
    dict = {}
    for log in record:
        command = log.split(' ')
        if 'Enter' in log:
            answer.append([command[1], "님이 들어왔습니다."])
            dict[command[1]] = command[2]
        elif 'Leave' in log:
            answer.append([command[1], "님이 나갔습니다."])
        else:
            dict[command[1]] = command[2]
    return(list(map(lambda x : dict[x[0]]+x[1], answer)))
