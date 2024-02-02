# https://leetcode.com/problems/3sum/


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1

        return answer
