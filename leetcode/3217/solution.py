class Solution:
    def removeElements(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy_head = ListNode(next=head)
        current_node = dummy_head
        
        while current_node and current_node.next:
            if current_node.next.val in nums_set:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next