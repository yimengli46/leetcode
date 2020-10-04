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
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        
        while True:
            if not head:
                break
            
            front = dummy
            tail = dummy.next
            flag_insert = False
            while True:
                #print('still in the inner while loop ...')
                if not tail:
                    tail = ListNode(head.val)
                    front.next = tail
                    flag_insert = True
                else:
                    val = tail.val
                    if val <= head.val:
                        front = tail
                        tail = tail.next
                    else:
                        node = ListNode(head.val)
                        #print('node.val = {}'.format(node.val))
                        #print('front.val = {}'.format(front.val))
                        #print('tail.val = {}'.format(tail.val))

                        front.next = node
                        node.next = tail
                        flag_insert = True

                if flag_insert:
                    break     
            
            head = head.next

        return dummy.next

#===================================================================================
li = [5, 4, 1, 2, 3]
head = tail = ListNode(0)
for i in li:
    node = ListNode(i)
    tail.next = node
    tail = tail.next
head = head.next

sol = Solution()
a = sol.insertionSortList(head)
print('result is :')
print_linked_list(a)




