# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        def linker(node: Optional[ListNode]):
            nonlocal head
            if node != None:
                if node.val == val:
                    return linker(node.next)
                else:
                    node.next = linker(node.next)
                    return node
            else:
                return None

        head = linker(head)
        return head