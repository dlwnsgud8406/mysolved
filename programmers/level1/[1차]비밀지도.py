def solution(n, arr1, arr2):
    answer = []
    arr = [['.' for i in range(n)] for i in range(n)]

    for i in range(n):
        code = bin(arr1[i] | arr2[i])[2:]
        final_code = ''
        length = len(code)
        print(length)
        while length < n:
            final_code += '0'
            length += 1
        final_code += code
        answer.append(final_code.replace('1', '#').replace('0', ' '))
    return answer

print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
