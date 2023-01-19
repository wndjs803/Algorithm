key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

lk = len(key)
lc = len(lock)
new_lock_size = (lk-1)*2 + lc

def rotate(key):
    new_key = [[0]*lk for _ in range(lk)]
    for i in range(lk):
        for j in range(lk):
            new_key[j][lk-i-1] = key[i][j]
    print(new_key)
    return new_key

def unlock(key, new_lock):
    n = new_lock_size - lk +1
    print(n)
    for i in range(n):
        for j in range(lk):
            for k in range(lk):
                print("sum = ")
                print(new_lock[j+i][k] + key[j][k])
                if new_lock[j+i][k] + key[j][k] != 1:
                    break
        return True
    return False

new_lock = [[0]*new_lock_size for _ in range(new_lock_size)]

for i in range(lc):
    for j in range(lc):
        new_lock[i+lc-1][j+lc-1] = lock[i][j]
print(new_lock)
ans = "false"
for i in range(4):
    if unlock(key, new_lock):
        ans = "true"
        break
    else:
        key = rotate(key)
        print(1)
print(ans)