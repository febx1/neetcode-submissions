class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"$"+i
        return res


    def decode(self, s: str) -> List[str]:
        ls,i=[],0
        
        while i <len(s):
            j=i
            while s[j]!="$":
                j+=1
            n=int(s[i:j])
            ls.append(s[j+1:j+1+n])
            i=j+1+n
        return ls


            
                

