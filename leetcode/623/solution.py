class Solution:
    def addOneRow(self, root: 'TreeNode', v: int, d: int) -> 'TreeNode':
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        
        level = 0
        queue = [root]
        
        while queue and level < d - 1:
            for _ in range(len(queue)):
                cur_node = queue.pop(0)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            level += 1
        
        for node in queue:
            left_child = node.left
            right_child = node.right
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = left_child
            node.right.right = right_child
        
        return root