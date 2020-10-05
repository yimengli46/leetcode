class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(node: ListNode):
    li = []
    while True:
        if node:
            li.append(node.val)
            node = node.next
        else:
            break
    print(li)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = tail = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                node = ListNode(list1.val)
                tail.next = node
                list1 = list1.next
            else:
                node = ListNode(list2.val)
                tail.next = node
                list2 = list2.next
            tail = tail.next

        while list1:
            node = ListNode(list1.val)
            tail.next = node
            list1 = list1.next
            tail = tail.next
        while list2:
            node = ListNode(list2.val)
            tail.next = node
            list2 = list2.next
            tail = tail.next

        return dummy.next

    def getMid(self, head):
        if not head:
            return head
        if head.next.next is None:
            slow = head.next
            head.next = None
            return slow
        slow_prev = slow = fast = head
        while fast.next and fast.next.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        slow_prev.next = None
        return slow

#=============================================================
li = [5, 4, 1, 2, 3,7,6]
head = tail = ListNode(0)
for i in li:
    node = ListNode(i)
    tail.next = node
    tail = tail.next
head = head.next

sol = Solution()
a = sol.sortList(head)
print('result is :')
print_linked_list(a)
