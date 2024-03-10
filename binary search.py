a = [0,1,2,3,4,5,6,7,8,9]
x = int(input("ENTER ELEMENT : "))
l=0
h=len(a)-1
c=0
while l<=h:
    m = (l+h)//2
    if a[m] == x:
        print("ELEMENT FOUND")
        print("Position : ", m+1)
        c=1
        break
    elif x>a[m]:
        l=m+1
    else:
        h=m-1
if c==0:
    print("ELEMENT NOT FOUND")
