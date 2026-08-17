class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+","*","-","/"]
        st = [int(tokens[0])]
        for t in tokens[1:]:
            if t in ops:
                num1 = st.pop()
                num2 = st.pop()

                if t == "+":
                    st.append(num2+num1)
                elif t == "-":
                    st.append(num2-num1)
                elif t == "*":
                    st.append(num2*num1)
                elif t == "/":
                    st.append(int(num2/num1))
            else:
                st.append(int(t))
        return st[0]