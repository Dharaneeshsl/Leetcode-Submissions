class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        data = data.split(",")
        self.i = 0
        
        def dfs():
            if data[self.i] == "null":
                self.i += 1
                return None
            
            node = TreeNode(int(data[self.i]))
            self.i += 1
            
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()