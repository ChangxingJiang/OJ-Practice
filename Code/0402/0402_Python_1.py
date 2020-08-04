class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        # 使用栈使每一位获得最小值
        for ch in num:
            n = int(ch)
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            if stack != [] or n != 0:
                stack.append(n)

        # 处理没有被用掉的k
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # 返回结果（若空栈则返回0）
        return "".join([str(n) for n in stack]) if stack else "0"


if __name__ == "__main__":
    print(Solution().removeKdigits(num="1432219", k=3))  # "1219"
    print(Solution().removeKdigits(num="10200", k=1))  # "200"
    print(Solution().removeKdigits(num="10", k=2))  # "0"
    print(Solution().removeKdigits(num="10", k=1))  # "0"
    print(Solution().removeKdigits(num="9", k=1))  # "0"
    print(Solution().removeKdigits(num="112", k=1))  # "0"
