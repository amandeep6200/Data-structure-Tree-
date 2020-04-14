def pair(a,b,k):
    a=list(set(a))
    dict={}
    for i in range(len(b)):
        dict[b[i]]=1
    print(dict)
    arr=[]
    for i in range(len(a)):
        val=k-a[i]
        if val in dict:
            arr.append((a[i],val))
    print(arr)        
               
            
a=[1,2,3,1]
b=[3,4,5,3]
k=6
pair(a,b,k)
