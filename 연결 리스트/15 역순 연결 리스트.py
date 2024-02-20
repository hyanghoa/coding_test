# https://leetcode.com/problems/reverse-linked-list/


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        while node:
            node_next, node.next = node.next, prev
            prev, node = node, node_next
        return prev
