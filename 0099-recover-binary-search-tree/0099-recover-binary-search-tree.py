class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first=None
        second=None
        prev=TreeNode(float("-inf"))
        def inorder(root):
            nonlocal first,second,prev
            if not root:
                return
            inorder(root.left)
            if prev.val>root.val:
                if not first:
                    first=prev
                second=root
            prev=root
            inorder(root.right)

        inorder(root)
        first.val,second.val=second.val,first.val