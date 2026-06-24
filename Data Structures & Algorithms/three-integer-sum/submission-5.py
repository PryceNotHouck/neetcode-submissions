# Follow Solution
# O(nlogn) time

# Sort input array
# Loop through values
    # Fix value for a
    # Perform two-pointer 2Sum on the sorted list after the fixed value for a
        # Left = b
        # Right = c
        # If a + b + c > 0, move left, a + b + c < 0, move right, append values otherwise unless dupe
# a + L + R = 0

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, a in enumerate(nums):  # i is index, a is value
            if i > 0 and a == nums[i - 1]:
                continue
                # Prevents using the same value for a twice

            left = i + 1
            right = len(nums) - 1
            while left < right:
                ts = a + nums[left] + nums[right]
                if ts > 0:
                    # Decrease sum -> move left
                    right -= 1
                elif ts < 0:
                    # Increase sum -> move right
                    left += 1
                else:
                    # If is equal to 0
                    results.append([a, nums[left], nums[right]])
                    # Copy of logic above to prevent using the same b twice
                    # The two pointer movements above acount for this for c automatically
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results