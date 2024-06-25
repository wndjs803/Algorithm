n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))
array.sort()

start = 1 # 최소 gap
end = array[n-1] - array[0] # 최대 gap
result = 0 # 가장 인접한 두 공유기 사이의 거리(gap)가 최대가 되어야 한다.

while start <= end:
    mid = (start + end) // 2
    value = array[0]
    count = 1 # 제일 첫 번째 좌표에 설치했다는 가정

    for i in range(1, n): # 1번 인덱스부터 체크
        if array[i] >= value + mid: # 만약 좌표 + gap 보다 크면 공유기 설치
            value = array[i]
            count += 1
    
    if count >= c: # c(준비된 공유기)보다 많이 설치가능하다는 것은 gap이 너무 작았다는 말 
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)