class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 0
        now = 0  # 当前各个数字的奇偶状态
        hashmap = {now: 0}  # 每个奇偶状态的最早出现坐标
        for i, ch in enumerate(s):
            # 计算当前数字添加后奇偶状态的变化
            now ^= 1 << int(ch)
            if now not in hashmap:
                hashmap[now] = i + 1

            # 计算当前奇偶状态构成回文串的最早坐标
            if now in hashmap:
                ans = max(ans, i - hashmap[now] + 1)
            for j in range(10):
                tmp = now ^ (1 << j)
                if tmp in hashmap:
                    ans = max(ans, i - hashmap[tmp] + 1)
            # print(i, "[", ch, "]", bin(now)[2:], "->", ans)

        return ans


if __name__ == "__main__":
    print(Solution().longestAwesome(s="3242415"))  # 5
    print(Solution().longestAwesome(s="12345678"))  # 1
    print(Solution().longestAwesome(s="213123"))  # 6
    print(Solution().longestAwesome(s="00"))  # 2
