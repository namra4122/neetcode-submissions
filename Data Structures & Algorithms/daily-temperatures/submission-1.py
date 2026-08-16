class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # n = len(temp)
        # res = [0]*n

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if temp[i] < temp[j]:
        #             res[i]= j-i
        #             break
        
        # return res

        st = [0]
        res = [0]*len(temp)

        for i in range(1, len(temp)):
            while(len(st) != 0 and temp[i] > temp[st[-1]]):
                idx = st.pop()
                res[idx] = i - idx
            st.append(i)
            
        
        return res