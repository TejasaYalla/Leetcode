class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in range(len(nums)):
            if i%2==0:
                a.append(nums[i])
            else:
                b.append(nums[i])
        a.sort(reverse= True)
        b.sort()
        print(a)
        print(b)
        for i in range(len(nums)):
            if i%2==0:
                nums[i]= a.pop()
            else:
                nums[i]= b.pop()
        return nums