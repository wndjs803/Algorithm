from collections import defaultdict

def solution(genres, plays):
    answer = []
    count = defaultdict(int)
    song = {}
    
    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        
        song.setdefault(genres[i], [])
        song[genres[i]].append((i, plays[i]))
    
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for key in sorted_count:
        sorted_song = sorted(song[key], key=lambda tup: (tup[1], -tup[0]), reverse=True)
        
        if len(sorted_song) < 2:
            answer.append(sorted_song[0][0])
        
        else:
            answer.append(sorted_song[0][0])
            answer.append(sorted_song[1][0])
    return answer