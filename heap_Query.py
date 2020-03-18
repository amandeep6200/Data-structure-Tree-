def heapify(heap,n,i):
    l=2*i+1
    r=2*i+2
    if l<n and heap[l]>heap[i]:
        largest=l 
    else:
        largest=i    
    if r<n and heap[r]>heap[largest]:
        largest=r 
    if largest!=i:
        heap[largest],heap[i]=heap[i],heap[largest]
        heapify(heap,n,largest)    

def heap_sort(heap):
    for i in range(len(heap)-1,0,-1):
        heap[i],heap[0]=heap[0],heap[i]
        heapify(heap,i,0)
    print(heap)    
def print_min(heap):
    for i in range(len(heap)):
        print(heap[i],end=" ")
def insert(heap,element):
    n=len(heap)+1
    heap.insert(n-1,element)
    heapify(heap,n,n-1)

t=int(input())
heap=[0]
for i in range(t):
    n=len(heap)
    arr=list(map(int,input().split()))
    if arr[0]==1:
        insert(heap,arr[1])
    if arr[0]==3:
        print_min(heap)
    if arr[0]==2:
        heap_sort(heap)
