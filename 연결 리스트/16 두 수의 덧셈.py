# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        list_l1 = []
        list_l2 = []
        while l1 or l2:
            if l1:
                list_l1.append(l1.val)
                l1 = l1.next
            if l2:
                list_l2.append(l2.val)
                l2 = l2.next

        list_sum = int("".join(map(str, list_l1[::-1]))) + int(
            "".join(map(str, list_l2[::-1]))
        )
        list_sum = list(str(list_sum))[::-1]

        answer = ListNode(list_sum[0])
        cur = answer
        for x in list_sum[1:]:
            cur.next = ListNode(x)
            cur = cur.next

        return answer
