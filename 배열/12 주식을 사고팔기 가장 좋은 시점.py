# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            answer = max(answer, price - min_price)
        return answer
