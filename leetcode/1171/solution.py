class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        
        prefix_sum_dict = {}
        current_sum = 0
        current_node = dummy
        
        while current_node:
            current_sum += current_node.val
            
            if current_sum in prefix_sum_dict:
                start_node = prefix_sum_dict[current_sum].next
                temp_sum = current_sum + start_node.val
                
                while start_node != current_node:
                    del prefix_sum_dict[temp_sum]
                    start_node = start_node.next
                    temp_sum += start_node.val
            
            prefix_sum_dict[current_sum] = current_node
            current_node = current_node.next
        
        return dummy.next