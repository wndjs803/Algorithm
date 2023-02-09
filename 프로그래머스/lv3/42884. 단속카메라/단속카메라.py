def solution(routes):
    routes.sort(key= lambda x:x[1])
    
    camera = -999999
    count = 0
    l = len(routes)
    for i in routes: 
        if camera < i[0]:
            camera = i[1]
            count +=1
    
    return count