class Solution:
    def findWords(self, board, words):
        root={}
        END="#"
        for w in words:
            node=root
            for ch in w:
                if ch not in node:
                    node[ch]={}
                node=node[ch]
            node[END]=w
        rows,cols=len(board),len(board[0])
        res=[]
        def dfs(r,c,node):
            ch=board[r][c]
            if ch not in node:
                return
            nxt=node[ch]
            if END in nxt:
                res.append(nxt[END])
                del nxt[END]
            board[r][c]="#"
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!="#":
                    dfs(nr,nc,nxt)
            board[r][c]=ch
            if not nxt:
                node.pop(ch)
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return res