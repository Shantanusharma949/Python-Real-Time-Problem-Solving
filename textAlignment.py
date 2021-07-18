n= int(input())
for i in range(1,2*n,2):
    str='H'*i
    print (str.center(2*n-1," "))

for i in range(n+1):
    str1='H'*n    
    print(str1.center(2*n-1," ")+" "*(2*n+1)+str1.center(2*n-1," "))
    
for i in range((n+1)//2):
    str=" "*((n-1)//2) +'H'*(n*5)
    print(str.center(n*5," "))
    
for i in range(n+1):
    str1='H'*n    
    print(str1.center(2*n-1," ")+" "*(2*n+1)+str1.center(2*n-1," "))
    
for i in range(2*n-1,0,-2):
    str='H'*i
    print (" "*4*n+str.center(2*n-1," "))
    