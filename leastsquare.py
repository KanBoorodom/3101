import copy

x = [0,10,20,30,40,50,60]
y = [-10,3,-7,6,10,1,15]
answer = -6.845, 0.314

""" 
x = [-1,0,1,2,4]
y = [3,1,1,0,4]
#answer = 1.184,-1.339,0.505
 """

ML,MR = [],[]
size = 2 #size = พหุนามกำลัง+1 ex.พหุนามกำลังสอง = สาม

def leastsquare(x,y,size = 2): #default linear least square size = 2
    global ML,MR
    for i in range(size):
        newList = []
        for j in range(size):
            if(i == 0 and j == 0):
                newList.append(len(x))
            else:
                pow = i+j
                sumPow = [ i ** pow for i in x]
                newList.append(sum(sumPow))
        ML.append(newList)
    #Calculate MR
    for i in range(size):
        #newList = []
        if(i == 0):
            #newList.append(sum(y))
            MR.append(sum(y))
        else:
            pow = i
            sumMul = [ (x[i] ** pow) * y[i] for i in range(len(y))]
            #newList.append(sum(sumMul))
            MR.append(sum(sumMul))
        #MR.append(newList)

def createAUX(a,b):
    aux = copy.deepcopy(a)
    for i in range(len(aux)):
        aux[i].append(b[i])
    return aux

def jordan(a,aux):
    for i in range(len(a[0])): #Row size ทำแค่ภายใน a ไม่วิ่งเกินไป b
        for j in range(len(aux)): #Column size วิ่งลงตาม column 
            if(j == i): #ตำแหน่่งที่ j == i คือเส้นทแยงมุม
                findMax = []
                for k in range(len(a[0])):
                    findMax.append(a[k][j])
                maxIndex = findMax.index(max(findMax))  #ถ้าค่าตัวเบขซ้ำกันตำแหน่ง max จะเป็นตำแหน่งของตัวแรก
                if(maxIndex > j):
                    temp = aux[j]
                    aux[j] = aux[maxIndex]
                    aux[maxIndex] = temp
                divide = aux[j][i] #ตัวหารเป็นหนึ่ง
                for k in range(len(aux[0])): #ตอนหารเป็นหนึ่งต้องหารทั้ง row
                    aux[j][k] = round(aux[j][k] / divide ,3)
            if(j > i):
                m = aux[j][i]
                for k in range(len(aux[0])):
                    aux[j][k] = round(aux[j][k] - (m * aux[i][k]),3)
    for i in range(len(a[0])-1,-1,-1):
        for j in range(len(aux)-1,-1,-1):
            if(j < i): #ทำแถวบนเส้นทแยงมุม แต่ไม่ทำแถวคำตอบ
                m = aux[j][i]
                for k in range(len(aux[0])): #j row k column #-2 เพื่อไม่รวม column คำตอบ
                    aux[j][k] = round(aux[j][k] - (m * aux[i][k]),3)
    return aux

leastsquare(x,y,size)
aux = createAUX(ML,MR)
answer = jordan(ML,aux)
for i in range(len(answer)):
    print(f'ANSWER: {answer[i][len(answer[0])-1]}')
