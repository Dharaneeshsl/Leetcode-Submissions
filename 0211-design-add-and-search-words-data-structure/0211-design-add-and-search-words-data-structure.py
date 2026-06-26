class WordDictionary:

    def __init__(self):
        self.ch={}
        self.isend=False
        self.root = self
        

    def addWord(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node.ch:
                node.ch[c]=WordDictionary()
            node=node.ch[c]
        node.isend=True
            
        

    def search(self, word: str) -> bool:
        return self.dfs(0,word,self.root)
        
    def dfs(self,i,word,node):
        if i==len(word):
            return node.isend
        c=word[i]
        if c!='.':
            if c not in node.ch:
                return False
            return self.dfs(i+1,word,node.ch[c])

        else:
            for x in node.ch.values():
                if self.dfs(i+1,word,x):
                    return True
            return False




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)