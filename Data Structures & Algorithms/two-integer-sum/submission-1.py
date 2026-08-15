class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc={}
        for i in range(len(nums)):
            r=target-nums[i]
            if r in dc:
                ind=dc[r]
                return [ind,i]
            dc[nums[i]]=i