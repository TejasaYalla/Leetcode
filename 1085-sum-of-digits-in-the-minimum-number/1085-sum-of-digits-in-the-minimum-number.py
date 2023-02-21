class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        x= min(nums)
        x=str(x)
        c=0
        for i in x:
            c+=int(i)
        if c%2==0:
            return 1
        else:
            return 0