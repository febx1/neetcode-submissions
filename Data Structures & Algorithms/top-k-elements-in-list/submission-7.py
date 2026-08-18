class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[[] for i in range(len(nums)+1)]
        dic={}
        rs=[]
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for n,v in dic.items():
            res[v].append(n)
        t=0
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                rs.append(j)
                t+=1
                if t==k:
                    return rs


