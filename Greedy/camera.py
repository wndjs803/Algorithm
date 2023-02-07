# routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
routes = [[-20, -15], [-18, -13], [-11, -8], [-14, -3], [-12, -5]]
routes.sort(key= lambda x:x[1])
print(routes)


camera = -999999
count = 0

for i in range(len(routes)):    
    if camera < routes[i][0]:
        camera = routes[i][1]
        count +=1
    print(camera)
print(camera)
print("count:", count)