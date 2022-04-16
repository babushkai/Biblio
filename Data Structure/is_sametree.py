def isSameTree(self, p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q       