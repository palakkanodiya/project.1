a=[1,9,2,8,3,7,6,4,5,0]
print("Unsorted array : ", a)
i=0
n=len(a)
while i<n-1:
    j=i+1
    while j < n:
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
        j=j+1
    i=i+1

print("SORTED ARRAY : ", a)
