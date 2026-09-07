# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        if not left and not right:
            return None
        if not left:
            return right
        if not right:
            return left
        

        if left.val < right.val:
            new = left
            left = left.next
            
        else:
            new = right        
            right = right.next
    
        otp = new
        

        while new:
            if not left:
                if right:
                    new.next = right
                    temp = right
                    right = right.next
                    new = temp
                    continue
                else:
                    break
            else:
                if not right:
                    new.next = left
                    temp = left
                    left = left.next
                    new = temp
                    continue
            l = left.val
            r = right.val
            print(l, r)
            # break

            if l < r:
                new.next = left
                temp = left
                left = left.next
                new = temp
                
                
            else:
                new.next = right
                temp = right
                right = right.next
                new = temp
        return otp
            






