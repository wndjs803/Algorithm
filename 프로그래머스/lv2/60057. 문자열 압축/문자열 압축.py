def solution(s):
    num = 0
    result = []
    a = []
    while num != len(s):
        num += 1
        j=0
        count = 1
        while True:
            tmp = s[j:j+(num)]
            cmp = s[j+num:j+2*num]
            if tmp == cmp:
                count += 1
            else:
                if count == 1:
                    result.append(tmp)
                else:
                    result.append(str(count) + tmp)
                    count = 1
                tmp = cmp
            j += num
            if j > len(s) or j+num > len(s):
                if count == 1:
                    result.append(s[j:len(s)])
                else:
                    result.append(str(count)+s[j:len(s)])

                break
        b = "".join(result)
        a.append([b, len(b)])
        result = []

    answer = min(a, key=lambda x :x[1])[1]
    return answer