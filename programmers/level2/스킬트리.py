def solution(skill, skill_trees):
    answer = 0
    arr = []
    compare_arr =[]
    compare_string = ''
    for char in skill:
        compare_string += char
        compare_arr.append(compare_string)
    compare_string = compare_string[::-1]
    for trees in skill_trees:
        string = ''
        for char in trees:
            if char in skill:
                string += char
        arr.append(string)

    for word in arr:
        if word in compare_arr or not len(word):
            answer += 1
    return answer
