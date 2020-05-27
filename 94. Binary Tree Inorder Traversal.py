# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# In order = Left Me Right
class Solution(object):
    """
    Iterative:
    Runtime: 12 ms, faster than 97.04%
    Memory Usage: 12.7 MB, less than 6.25%

    https://leetcode.com/problems/binary-tree-inorder-traversal/
    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        results = []
        stack = []
        
        curr_node = root
        
        while curr_node or stack:
            if curr_node:    # keep going left until we reach a leaf, adding each node to stack on the way
                stack.append(curr_node) 
                curr_node = curr_node.left
                
            else:  # current node is non existent, its parent is a leaf
                curr_node = stack.pop()   # pop that leaf parent from the stack and save it
                results.append(curr_node.val)   # add its value to results
                
                # go to the right
                # if you're at a leaf node, it's not going to have a right, so root will be None
                # next round in the while loop,  the code will reach the else section again (line 32)
                # and it will pop the next thing on the stack, which is the "me" node in "left, me, right"
                # then, this round, the next root will be assigned to "me"'s right node, and cycle continues
                curr_node = curr_node.right
        return results