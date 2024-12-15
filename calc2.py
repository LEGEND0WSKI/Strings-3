# Time:O(n)
# Space:O(1)
# Leetcode:Yes
# Issues:No

class Solution:
    def calculate(self, s: str) -> int:
        calc, tail, curr = 0,0,0
        sign = '+'

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                curr = 10* curr + (ord(c)- ord('0'))

            if not c.isdigit() and c!=' ' or i == len(s)-1:
                if sign == '+':
                    calc = calc + curr
                    tail = curr
                elif sign == '-':
                    calc = calc - curr
                    tail = -curr
                elif sign == "*":
                    calc = (calc-tail) + (tail * curr)
                    tail = tail*curr
                elif sign == '/':
                    calc = (calc-tail) + int(tail /curr)
                    tail = int(tail/curr)
                sign = c
                curr = 0
            
        return calc
    
# with stack// T:O(n); S:O(n)
class Solution:
    def calculate(self, s: str) -> int:
        st = []
        curr = 0
        sign = "+"

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                curr = 10 * curr + (ord(c) - ord('0'))
            
            if (not c.isdigit() and c!=" ") or i == len(s)-1:
                if sign == '+':
                    st.append(curr)
                elif sign == '-':
                    st.append(-curr)
                elif sign == '*':
                    x = st.pop()
                    st.append(x*curr)
                elif sign == '/':
                    x = st.pop()
                    st.append(int(x/curr))
                curr = 0
                sign = c
        return sum(st)               