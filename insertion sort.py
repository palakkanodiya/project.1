a = [1,9,2,8,3,7,4,6,5,0]
print("Unsorted array : ", a)
n = len(a)
i=1
while i<n:
    x = a[i]
    j = i-1
    while j>=0:
        if a[j] > x:
            a[j+1] = a[j]
        else:
            break
        j=j-1
    a[j+1]=x
    i=i+1

print("SORTED ARRAY : ", a)
