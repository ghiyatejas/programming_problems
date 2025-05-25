class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def has_cycle(self, head):
        try:
            if head is None or head.next is None:
                return False
            
            slow = head
            fast = head
            
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    return True
            
            return False
        except Exception as ex:
            print(ex)
            return False
