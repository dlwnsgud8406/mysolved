from collections import defaultdict

genres=["classic", "pop", "classic", "classic", "pop", "hip", "hip"]	
plays=[500, 600, 150, 800, 2500, 1300, 1000]
music_list = []
# set으로 전환해줘야함
for i in range(len(plays)):
    music_list.append((genres[i], plays[i]))

music_dict = defaultdict(list)

for k, v in music_list:
    music_dict[k].append(v)

print((music_dict.values()))

# print(music_dict(music_dict.keys()).values())