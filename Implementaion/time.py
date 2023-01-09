n = int(input())

time = (n+1)*60*60
time_s = 0
time_m = 0
time_h = 0
count = 0
for i in range(time):
    time_s += 1
    if "3" in str(time_s) or "3" in str(time_m) or "3" in str(time_h):
        count +=1
    if(time_s == 60):
        time_m +=1
        time_s = 0
    if(time_m == 60):
        time_h +=1
        time_m = 0
    
print(time_h, time_m, time_s)
print(count)
