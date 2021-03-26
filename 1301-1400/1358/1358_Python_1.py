class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        left = -1  # 窗口左侧坐标
        a, b, c = -1, -1, -1  # 当前最近的a,b,c坐标
        ans = 0
        for right, ch in enumerate(s):
            # 更新最近的a,b,c坐标
            if ch == "a":
                a = right
            elif ch == "b":
                b = right
            else:
                c = right

            # 判断窗口内是否包含三个字母
            if a > left and b > left and c > left:
                new_left = min(a, b, c)
                ans += (new_left - left) * (N - right)
                left = new_left

        return ans


if __name__ == "__main__":
    print(Solution().numberOfSubstrings(s="abcabc"))  # 10
    print(Solution().numberOfSubstrings(s="aaacb"))  # 3
    print(Solution().numberOfSubstrings(s="abc"))  # 1
