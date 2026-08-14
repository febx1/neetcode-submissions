class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a=[0 for i in range(26)]
        b=[0 for i in range(26)]
        for i in s.lower():
            a[ord(i)-97]+=1
        for i in t.lower():
            b[ord(i)-97]+=1
        if a==b:
            return True
        
        return False