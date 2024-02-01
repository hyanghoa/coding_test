# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        result = 0

        for idx, h in enumerate(height):
            if stack:
                if stack[-1][1] < h:
                    while stack:
                        volume = stack.pop()
                        if volume[1] >= h:
                            stack.append(volume)
                            break
                        if len(stack) == 0:
                            break
                        if stack[-1][1] > volume[1]:
                            block_height = min(h, stack[-1][1])
                            distance = idx - stack[-1][0] - 1
                            result += (block_height - volume[1]) * distance
                stack.append((idx, h))
            else:
                stack.append((idx, h))
        return result
