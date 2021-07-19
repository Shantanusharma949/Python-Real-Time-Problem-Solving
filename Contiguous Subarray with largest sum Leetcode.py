#Given an integer subarray, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum
#EXAMPLES
#[-2,1,-3,4,-1,2,1,-5,4]==> 6
#[1]==> 1
#[5,4,-1,7,8]==> 23

x=list(map(int,input().split()))
sum=0
max_sum=0
for i in x:
    sum=sum+i
    if max_sum<sum:
        max_sum=sum
    elif sum<0:
        sum=0

print(max_sum)

