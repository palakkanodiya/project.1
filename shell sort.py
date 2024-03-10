a=[1,9,2,8,7,3,4,6,5,0]
print("Unsorted array : ", a)
n = len(a)
span = n//2
while span>=1:
    k=0
    while k<span:
        i=k+span
        while i<n:
            x=a[i]
            j=i-span
            while j>=0:
                if a[j]>x:
                    a[j+span] = a[j]
                else:
                    break
                j = j-span
            a[j+span] = x
            i = i+span
        span = span//2

print("SORTED ARRAY : ", a)
