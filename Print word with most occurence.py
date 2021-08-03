from collections import OrderedDict
class Solution:
    
    
    def mostFrequentWord(self,arr,n):
        d=OrderedDict()
        for i in arr:
            if i not in d.keys():
                d[i]=arr.count(i)
        max=0
        word=""
        for key,value in d.items():
            if value>=max:
                max=value
                word=key
        return word
                
            
n=int(input())
arr=[x for x in input().strip().split()]
obj = Solution()
print(obj.mostFrequentWord(arr,n))


#YOU CAN USE THIS CLASS ALSO FOR BETTER EFFICIENCY OF THE CODE
#from collections import Counter
#class Solution:
#    def mostFrequentWord(self,arr,n):
#        dict1=Counter(arr)
#
#        max1=max(dict1.values())
#
#        return arr[max([arr.index(i) for i in list(filter(lambda x:dict1[x]==max1,dict1))])]
                