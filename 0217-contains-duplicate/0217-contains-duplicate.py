class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # 1. Understand: 
          # Can the input array be empty? -> NO
        # 2. Match:
          # Storing the elements of the array in a HashMap or a Set.
          # If the number is already is in the set, return true otherwise false
        # 3. Plan
            # 1. Create a set to store number
            # 2. Iterate thorugh numbers
                # if number is already in set return True
                # else store number in set
            # return False (reached the end of list without duplicates)
        # 4. Implement 
        
        # Create set
        hashSet = set()
    
        # Iterate thorugh numbers
        for num in nums:
            if num in hashSet:
                return True
            # store the number in set
            hashSet.add(num)

        # Return flase since we reached end of list wihtout duplicates
        return False


    # Review:
        # No issues,code passed
    # Evaluate
        # Time Complexity: O(N) because we need to traverse all numbers in the array.
        # Space Complexity: O(N) because we may need to store all numbers in the array.

        