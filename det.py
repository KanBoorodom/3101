#DET AND PIVOT AND GAUSSIAN ELIMINATION
""" a = [
        [0, 0, 2],
        [6, 0, 0],
        [0, 4, 0]
    ]
 """
a = [
        [2, 0, 4],
        [3, 2, 1],
        [4, 4, 2]
    ]


for i in range(len(a[0])): #row
    for j in range(len(a)): #col
        #print(a[i][j]) #วิ่งตามแนว row
        #print(a[j][i]) #วิ่งตามแนว col
        if(j == i):
            #PIVOT-------------------------------------------------
            findMax = []
            for k in range(len(a[0])):
                findMax.append(a[k][j])
            maxIndex = findMax.index(max(findMax))
            if(maxIndex > j):
                #print(a[maxIndex][j])
                temp = a[j]
                a[j] = a[maxIndex]
                a[maxIndex] = temp
            upValue = a[j][i] #ค่าที่เส้นทแยง
        #GAUSSIAN START-------------------------------------------------
        if(j > i):
            downValue = a[j][i]
            m = downValue / upValue
            for k in range(len(a[0])):
                a[j][k] = round( a[j][k] - (m * a[i][k]) , 2)

print('FIND DET--------------')
det = 1
for i in range(len(a[0])): 
    for j in range(len(a)): 
        if(j == i):
            det*=a[j][i]
print(a)
print(det)
