# https://leetcode.com/problems/product-of-array-except-self/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left_list = [1]
        right_list = [1]

        for i in range(len(nums)):
            left_list.append(left_list[-1] * nums[i])
            right_list.insert(0, right_list[0] * nums[-i - 1])

        for x, y in zip(left_list[:-1], right_list[1:]):
            answer.append(x * y)

        return answer
