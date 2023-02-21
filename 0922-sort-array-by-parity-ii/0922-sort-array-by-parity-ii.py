class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        final=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        for i in range(len(nums)):
            if i%2==0:
                final.append(a.pop())
            else:
                final.append(b.pop())
        return final
                
        