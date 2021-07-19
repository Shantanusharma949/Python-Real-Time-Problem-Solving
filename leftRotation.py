
n,k=input().split()
n=int(n)
k=int(k)

l=list(map(int,input().split()))
    
while k:
    temp=l[0]
    for i in range(0,len(l)-1):
        l[i]=l[i+1]
    k=k-1
    l[n-1]= temp
for i in range(0,len(l)):
    print(l[i],end=" ")
    
    
        


    