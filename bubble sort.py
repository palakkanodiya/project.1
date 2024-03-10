a = [1,9,2,8,3,7,4,6,5,0]
print("Unsorted array : ", a)
n = len(a)
i = n-1
while i>=1:
    j=0
    while j<i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j=j+1
    i=i-1
print("SORTED ARRAY : ", a)
