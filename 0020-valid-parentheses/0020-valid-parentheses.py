class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch in '{[(':
                stack.append(ch)
            elif len(stack)==0:
                return False
            elif (ch==')' and stack[-1]=='(') or (ch=='}' and stack[-1]=='{') or (ch==']' and stack[-1]=='['):
                stack.pop()
            else:
                return False 
            
        return len(stack)==0