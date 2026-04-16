class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        appeared = set()

        for n in nums:
            if n in appeared:
                appeared.remove(n)
            else:
                appeared.add(n)
        
        #return list(appeared)[0]
        return list(appeared)[0]
            

        