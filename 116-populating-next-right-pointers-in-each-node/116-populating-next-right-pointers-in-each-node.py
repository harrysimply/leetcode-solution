"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        完美二叉树：根节点左右两侧都有节点。
        本题要求所有层级左边的节点都指向右侧的节点，右侧节点如果不为空则连线右侧树节点的左侧
        实现一个树链表 哈哈
        
        使用深度优先搜索
        '''
        
        if not root:
            return 
        if root.right:
            root.left.next = root.right
            # 第三层的情况，如果root的next不为空，则下一层的右侧节点一定指向root的next的left
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
        
        
        