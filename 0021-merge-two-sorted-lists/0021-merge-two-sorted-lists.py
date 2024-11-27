# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None: return list2
        elif list2 is None: return list1
        else:
            if list1.val <= list2.val:
                head = list1
                other_node = list2
            else: 
                head = list2
                other_node = list1
            current_node = head
            while current_node.next is not None or other_node is not None:
                if current_node.next is None:
                    current_node.next = other_node
                    break
                if other_node is None: break
                if current_node.next.val < other_node.val:
                    current_node = current_node.next
                else:
                    temp_node = current_node.next
                    current_node.next = other_node
                    current_node = current_node.next
                    other_node = temp_node
            return head
            
