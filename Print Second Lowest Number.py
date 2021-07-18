names=[]
marks=[]
dict={}

for i in range(int(input())):
    name=input()
    mark=int(input())
    names.append(name)
    marks.append(mark)
    dict[name]=mark

marks=set(marks) #all common mark in marks are removed(property of set)
marks=list(marks)
marks.sort()
sec_low=marks[1]

for k, value in dict.items():
    if value==sec_low:
        print(k)

