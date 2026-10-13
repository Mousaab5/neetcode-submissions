class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frq = {}
        for x in nums:
            if x in frq:
                frq[x]+=1
            else:
                frq[x]=1
        for x in frq:
            if frq[x]>1:
                return True
        return False