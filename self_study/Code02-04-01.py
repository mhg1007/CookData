def multi(v1,v2):
    retList=[]
    res1=v1+v2
    res2=v1-v2
    res3=v1*v2
    res4=v1//v2
    res5=v1%v2
    res6=v1**v2
    retList.append(res1)
    retList.append(res2)
    retList.append(res3)
    retList.append(res4)
    retList.append(res5)
    retList.append(res6)
    return retList

myList=[]
r1,r2,r3,r4,r5,r6=0,0,0,0,0,0

myList=multi(100,20)
r1=myList[0]
r2=myList[1]
r3=myList[2]
r4=myList[3]
r5=myList[4]
r6=myList[5]
print("multi()에서 반환한 값 ==> %d, %d, %d, %d, %d, %d" % (r1,r2,r3,r4,r5,r6))
