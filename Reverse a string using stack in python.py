def createStack():
    stack=[]
    return stack
 
def isEmpty(stack):
    if size(stack) == 0:
        return true
 

def push(stack,item):
    stack.append(item)
 

def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
 

def reverse(string):
    n = len(string)
     
    
    stack = createStack()
 
    
    for i in range(0,n,1):
        push(stack,string[i])
 
    string=""
 
    for i in range(0,n,1):
        string+=pop(stack)
         
    return string

def size(stack):
    return len(stack)
     

string=input()
string = reverse(string)
print("Reversed string is " + string)
