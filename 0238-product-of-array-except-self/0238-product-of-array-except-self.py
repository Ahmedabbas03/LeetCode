class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]  # Update the result array with the product of elements to the left
            res[i] *= left_product  # Update the running product for the next iteration

        # Calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            res[i] *= right_product

        return res