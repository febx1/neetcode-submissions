class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            r=target-nums[i]
            if r in dic:
                return [dic[r],i]
            dic[nums[i]]=i
        
