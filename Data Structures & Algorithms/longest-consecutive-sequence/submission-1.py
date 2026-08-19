class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        longest=0
        for i in nums:
            if i-1 not in st:
                length=1
                while i+1 in st:
                    i+=1
                    length+=1
                longest=max(longest,length)
        return longest
