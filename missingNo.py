class Solution:
    def missingNum(self, arr):
        n = len(arr)+1
        expSum = (n*(n+1))//2
        actSum = sum(arr)
        
        return expSum-actSum
