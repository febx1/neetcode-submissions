class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        res=[[] for i in range(len(nums)+1)]
        resv=[]
        for n in nums:
            dic[n]=dic.get(n,0)+1
        for n,c in dic.items():
            res[c].append(n)
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                resv.append(j)
                if len(resv)==k:
                    return resv
        
        

