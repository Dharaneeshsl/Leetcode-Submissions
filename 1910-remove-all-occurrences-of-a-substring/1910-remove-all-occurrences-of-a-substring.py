class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st=[]
        m=len(part)
        for c in s:
            st.append(c)
            if len(st)>=m and "".join(st[-m:])==part:
                for _ in range(m):
                    st.pop()

        return "".join(st)