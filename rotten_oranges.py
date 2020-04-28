'''

def rotten_orange(mat,r,c):
    que=[]
    #enqueing all the 2's
    for i in range(r):
        for j in range(c):
            if mat[i][j]==2:
                que.append([i,j])
    time=0
    while que:
        curr_len=len(que)
        while curr_len:
            curr_len-=1
            
            x,y=que.pop(0)
    
            #checking neighbour of the rotten orange
            if x>0 and mat[x-1][y]==1:
                mat[x-1][y]=2
                que.append([x-1,y])
            if y>0 and mat[x][y-1]==1:
                mat[x][y-1]=2
                que.append([x,y-1])
            if x<r-1 and mat[x+1][y]==1:
                mat[x+1][y]=2
                que.append([x+1,y])
            if y<c-1 and mat[x][y+1]==1:
                mat[x][y+1]=2
                que.append([x,y+1])
        time+=1
    #checking if there are any 1's left
    for row in mat:
        if 1 in row:
            return -1
    #else time
    return time-1
    
for i in range(int(input())):
    r,c=input().split()
    mat=[[0 for i in range(int(c))]for i in range(int(r))]
    arr=list(map(int,input().split()))
    k=0
    for i in range(int(r)):
        for j in range(int(c)):
            mat[i][j]=arr[k]
            k+=1
    
    print(rotten_orange(mat,int(r),int(c)))





















'''
def rotten_orange(mat,r,c):
    que=[]
    for i in range(r):
        for j in range(c):
            if mat[i][j]==2:
              que.append([i,j])          
    t=0        
    while que:
      curr_len=len(que)  
      while curr_len:
             x,y=que.pop(0)
             
             if x>0 and mat[x-1][y]==1:
                mat[x-1][y]=2
                que.append([x-1,y])
             if y>0 and mat[x][y-1]==1:
                mat[x][y-1]=2
                que.append([x,y-1])
             if x<r-1 and mat[x+1][y]==1:
                mat[x+1][y]=2
                que.append([x+1,y])
             if y<c-1 and mat[x][y+1]==1:
                mat[x][y+1]=2
                que.append([x,y+1])
             curr_len-=1
      t+=1       
    for i in mat:
        if 1 in i:
            return -1
    return t-1    
        
                     
for i in range(int(input())):
        r,c=map(int,input().split())
        arr=list(map(int,input().split()))       
        mat=[[0 for i in range(c)]for j in range(r)]
        k=0       
        for i in range(r):
               for j in range(c):
                  mat[i][j]=arr[k]
                  k+=1
        print(rotten_orange(mat,r,c))       
        
