class Solution:
    def minCut(self, s):
        size = len(s)

        # 计算是否为回文串
        is_palindrome = [[False] * size for _ in range(size)]
        for r in range(size):
            for l in range(r, -1, -1):
                if s[l] == s[r] and (r - l <= 2 or is_palindrome[l + 1][r - 1]):
                    is_palindrome[l][r] = True

        # 动态规划计算结果
        dp = [i for i in range(size)]
        for i in range(1, size):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = min(dp[j] + 1 for j in range(i) if is_palindrome[j + 1][i])

        return dp[-1]


if __name__ == "__main__":
    # 1
    print(Solution().minCut("aab"))

    # 452
    print(Solution().minCut(
        "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"))
