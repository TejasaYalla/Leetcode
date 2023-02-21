class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i<0:
                b.append(i)
            else:
                a.append(i)
        for i in range(len(nums)):
            if i%2==0:
                nums[i]= a.pop(0)
            else:
                nums[i]= b.pop(0)
        return nums
                