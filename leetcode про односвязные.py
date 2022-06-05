# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def append(self, val):
        end = ListNode(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         n1=l1
#         n2=l2
#
#         a1=0
#         mul=1
#         while n1.next:
#             a1+=n1.val*mul
#             mul*=10
#             n1=n1.next


ll=ListNode(2)
ll.append(4)
ll.append(3)

node = ll
print(node.val)
while node.next:
    node = node.next
    print(node.val)

ll2=ListNode(5)
ll2.append(6)
ll2.append(4)

node = ll2
print('ll2=',node.val, end=' ')
while node.next:
    node = node.next
    print(node.val, end=' ')



