class Solution:
    def longestAwesome(self, s: str) -> int:
        status = 0  # 当前各个数字的奇偶状态
        hashmap = {status: [0, 0]}  # 每个奇偶状态的最早出现坐标
        for i, ch in enumerate(s):
            # 计算当前数字添加后奇偶状态的变化
            status ^= 1 << int(ch)
            if status not in hashmap:
                hashmap[status] = [i + 1, i + 1]
            else:
                hashmap[status][1] = i + 1

        # 计算当前奇偶状态构成回文串的最早坐标
        ans = 1
        for status in hashmap:
            ans = max(ans, hashmap[status][1] - hashmap[status][0])
            for j in range(10):
                if (tmp := status ^ (1 << j)) in hashmap:
                    ans = max(ans, hashmap[status][1] - hashmap[tmp][0])

        return ans


if __name__ == "__main__":
    print(Solution().longestAwesome(s="3242415"))  # 5
    print(Solution().longestAwesome(s="12345678"))  # 1
    print(Solution().longestAwesome(s="213123"))  # 6
    print(Solution().longestAwesome(s="00"))  # 2
