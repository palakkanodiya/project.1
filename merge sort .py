def mergeSort(arr):
    size = 1
    n = len(arr)
    while (size < n):
        l1 = 0
        k = 0
        c=[]
        while l1+size < n:
            u1 = l1+size-1
            l2 = u1+1
            if l2+size-1 < n:
                u2 = l2+size -1
            else:
                u2 = n-1
            i=l1
            j=l2
            while(i<=u1 and j<=u2):
                if arr[i] < arr[j]:
                    c.append(arr[i])
                    i+=1
                else:
                    c.append(arr[j])
                    j+=1
                k+=1
            while i<=u1:
                c.append(arr[i])
                i+=1
                k+=1
            while j<=u2:
                c.append(arr[j])
                j+=1
                k+=1
            l1 = u2+1        
        while(k<n):
            c.append(arr[k])
            k+=1
        for i in range(0, n):
            arr[i] = c[i]
        size = size * 2
    print("After sorting : ", arr)   

arr = [9,2,50,63,24,70,100,30,5,3,7]
#arr = [2,9,9,7,9,2,4,5,8]
print("Before sorting : ", arr)
mergeSort(arr)