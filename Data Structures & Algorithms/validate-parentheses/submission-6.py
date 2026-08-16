class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        m = {')':'(', ']':'[', '}':'{'}

        for br in s:
            if br in m:
                if st and st[-1] == m[br]:
                    st.pop()
                else:
                    return False
            else:
                st.append(br)

        return False if st else True