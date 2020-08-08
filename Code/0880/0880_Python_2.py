class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # 统计最终解码字符串长度
        size = 0
        for ch in S:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        # 不断逆向取模简化索引
        for ch in reversed(S):
            K %= size
            if K == 0 and ch.isalpha():
                return ch

            if ch.isdigit():
                size /= int(ch)
            else:
                size -= 1


if __name__ == "__main__":
    print(Solution().decodeAtIndex(S="leet2code3", K=10))  # "o"
    print(Solution().decodeAtIndex(S="ha22", K=5))  # "h"
    print(Solution().decodeAtIndex(S="a2345678999999999999999", K=1))  # "a"
    print(Solution().decodeAtIndex(S="a2b3c4d5e6f7g8h9", K=10))  # c
    print(Solution().decodeAtIndex(S="y959q969u3hb22odq595", K=222280369))  # 7
