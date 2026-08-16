class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for br in s:
            if br in ['(','[','{']:
                st.append(br)
            else:
                if len(st) != 0:
                    top = st.pop()
                else:
                    return False
                if top == '(' and br == ')':
                    continue
                elif top == '[' and br == ']':
                    continue
                elif top == '{' and br == '}':
                    continue
                else:
                    return False
        
        return True if len(st) == 0 else False