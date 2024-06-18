class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        numsSet = set(nums)
        res = 0

        for num in nums:
            if (num + diff in numsSet) and (num + 2 * diff in numsSet):
                res += 1

        return res
     