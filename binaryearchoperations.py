class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
        if root is None or root.val==key:
            return root
        if root.data<key:
           return  search(root.right,key)
        return search(root.left,key)
def insertion(root,Node):
        if root is None:
            root=Node
        if root.data<Node.data:
            if root.right is None:
                root.right=Node
            else:
                insertion(root.right,Node)
        else:
            if root.left is None:
                root.left=Node
            else:
                insertion(root.left,Node)
def inorder(root): 
       if root:
         print(root.data)   
         inorder(root.left) 
         inorder(root.right)
def levelOrder(root):
    if root is None: 
        return
    queue=[]
    queue.append(root)
    
    while len(queue)>0:
        print(queue[0].data)
        curr=queue.pop(0)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
            
def Kth_level(root,level):
    if root is None:
        return None
    if level==0:
        print( root.data,end=" ")
    Kth_level(root.left,level-1)
    Kth_level(root.right,level-1)
    
    
def minValueNode(node):
    current = node 
    while(current.left is not None): 
        current = current.left  
    return current
def children_sum(root):
    if root==None:
        return True
    if root.left==None and root.right==None:
        return True
    sum=0
    if root.left!=None:
        sum+=root.left.data
    if root.right!=None:
        sum+=root.right.data
    if sum==root.data and children_sum(root.left) and children_sum(root.right):
        return True
    else:
        return False
    
def height_BST(root):
    if root==None:
        return 0
    else:
      hl= height_BST(root.left)
      hr= height_BST(root.right)
      return max(hr,hl)+1
def balanced_tree(root):
        if root is None:
          return True
    
        lh=height_BST(root.left)
        rh=height_BST(root.right)
        if (abs(lh - rh) <= 1) and balanced_tree(root.left) is True and balanced_tree( root.right) is True: 
          return True
        else:
          return False
        
def deletion(root,key):
    if root is None:
        return root
    elif key<root.data:
        root.left=deletion(root.left,key)
    elif key>root.data:
        root.right=deletion(root.right,key)
    else:
         if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
         elif root.right is None : 
            temp = root.left  
            root = None
            return temp
         temp = minValueNode(root.right)  
         root.key = temp.key 
         root.right = deleteNode(root.right , temp.key) 
  
  
    return root
def storeInoder(root,arr):
    if root==None:
       return 
    storeInoder(root.left,arr)
    arr.append(root.data)
    storeInoder(root.right,arr)
def checkBST(root):
    arr=[]
    storeInoder(root,arr)
    temp=arr
    print("arr",arr)
    if temp==sorted(arr):
        return "Yes"
    else:
        return "No"
    
            
r=Node(50)
insertion(r,Node(30))
insertion(r,Node(20))
insertion(r,Node(40))
insertion(r,Node(70))
insertion(r,Node(60))
insertion(r,Node(80))
inorder(r)
deletion(r,40)
print("After deletion")
inorder(r)
print("levelorder traversal")
levelOrder(r)
print("Height of tree")
print(height_BST(r))
print(children_sum(r))
if balanced_tree(r):
    print("Balanced Tree")
else:
    print("Not Balanced Tree")
Kth_level(r,2)
print(checkBST(r))


                   
                             
                             
              
             
            
        
