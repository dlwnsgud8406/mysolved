def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]]) # dict형 (plays, index)
    genreSort = sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


genres=["classic", "pop", "classic", "classic", "pop", "hip", "hip"]	
plays=[500, 600, 150, 800, 2500, 1300, 1000]
print(solution(genres, plays))
solution(genres, plays)