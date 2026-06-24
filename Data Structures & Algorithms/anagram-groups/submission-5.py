class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            a=[0]*26
            for j in i: 
                a[ord(j)-ord('a')]+=1
            dic[tuple(a)].append(i)
        print(dic.values())
        return list(dic.values())
