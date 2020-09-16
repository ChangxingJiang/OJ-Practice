class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        stack = []
        idx = 0
        size = len(S)
        while idx < size and len(stack) < K:
            if S[idx].isalpha():
                stack.append(S[idx])
            else:
                num = int(S[idx])
                now = len(stack)
                for _ in range(num - 1):
                    for i in range(now):
                        stack.append(stack[i])
                        if len(stack) >= K:
                            break
            idx += 1
        return stack[K - 1]


if __name__ == "__main__":
    print(Solution().decodeAtIndex(S="leet2code3", K=10))  # "o"
    print(Solution().decodeAtIndex(S="ha22", K=5))  # "h"
    print(Solution().decodeAtIndex(S="a2345678999999999999999", K=1))  # "a"
    print(Solution().decodeAtIndex(S="a2b3c4d5e6f7g8h9", K=10))  # c
    print(Solution().decodeAtIndex(S="y959q969u3hb22odq595", K=222280369))  # c
