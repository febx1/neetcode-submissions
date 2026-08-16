class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        dic={}
        for i in strs:
            a=[0]*26
            for j in i:
                ind=ord(j)-ord('a')
                a[ind]+=1
            r=dic.get(tuple(a),[])
            r.append(i)
            dic[tuple(a)]=r
        res=[value for key,value in dic.items()]
        return res


