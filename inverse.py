#INVERSE NO PIVOT
import copy 
a = [   [3,12,8],
        [4,10,5],
        [9,11,13]
    ]
b = [   [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
aux = copy.deepcopy(a)

for i in range(len(aux)):
    for j in range(len(b[0])):
        aux[i].append(b[i][j])
print(aux)

for i in range(len(a[0])): #Row size ทำแค่ภายใน a ไม่วิ่งเกินไป b
    for j in range(len(aux)): #Column size วิ่งลงตาม column 
        if(j == i): #ตำแหน่่งที่ j == i คือเส้นทแยงมุม
            divide = aux[j][i] #ตัวหารเป็นหนึ่ง
            for k in range(len(aux[0])):
                aux[j][k] = round(aux[j][k] / divide ,2)
        if(j > i):
            m = aux[j][i]
            for k in range(len(aux[0])): #ตอนเปลี่ยนค่าต้องเปลี่ยนค่าทั้ง row
                #print(f'{aux[j][k]} - {m}*{aux[i][k]}')
                #print('----------------------------------------')
                aux[j][k] = round(aux[j][k] - (m * (aux[i][k])),2) #อย่าลืมคูณ m 
print(aux)
print('DONE LOWER-----------------------------')
for i in range(len(a[0])-1, -1, -1):
    for j in range(len(aux)-1, -1, -1):
        if(j < i):
            m = aux[j][i]
            for k in range(len(aux[0])):
                aux[j][k] = round(aux[j][k] - (m * aux[i][k]),2)
print(aux)
print('DONE UPPER-----------------------------')

print('REVERSE-----------------------------')
for i in aux:
    print(i)
