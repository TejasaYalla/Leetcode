class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        inserted=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[inserted]=nums[i]
                inserted+=1
        return inserted