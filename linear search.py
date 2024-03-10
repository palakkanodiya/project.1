a = [1,9,2,8,3,7,6,4,5,0]
x = int(input("ENTER ELEMENT : "))
i=0
c=0
while i<len(a):
    if a[i] == x:
        print("ELEMENT FOUND")
        print("Position : ", i+1)
        c=1
        break
    else:
        i=i+1
if c==0:
    print("ELEMENT NOT FOUND")
