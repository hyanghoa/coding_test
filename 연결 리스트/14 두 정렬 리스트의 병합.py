# https://leetcode.com/problems/palindrome-linked-list/


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        cur = head
        while cur:
            result.append(cur.val)
            cur = cur.next

        return result == result[::-1]
