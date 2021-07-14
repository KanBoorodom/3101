import math

data =  [ [2,0.5], 
          [2.5,0.4],
          [4,0.25]    
        ]
p = 3 

sumResult = []
for i in range(len(data)):
    up = []
    down = []
    for j in range(len(data)):
        if(j != i):
            up.append(p - data[j][0])
            down.append(data[i][0] - data[j][0])
    upResult = math.prod(up)
    downResult = math.prod(down)
    sumResult.append(round(upResult / downResult,3))
for i in range(len(sumResult)):
    sumResult[i]*=data[i][1]

print(sum(sumResult))
