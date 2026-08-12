class Solution(object):
    def inorderTraversal(self, root):
        stack = []
        tree = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            tree.append(cur.val)
            cur = cur.right
        return tree