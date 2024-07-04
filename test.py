def plus(v1,v2):
    result=0
    result=v1+v2
    return result

hap=0

while True:
    a=int(input("a:"))
    b=int(input("b:"))
    hap=plus(a,b)
    print("%d + %d = %d" % (a,b,hap))

