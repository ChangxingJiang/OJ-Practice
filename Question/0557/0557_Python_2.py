class Solution:
    def reverseWords(self, s: str) -> str:
        last = 0
        ans = ""
        for i in range(len(s)):
            if s[i] == " ":
                ans += s[last:i][::-1] + " "
                last = i + 1
        else:
            ans += s[last:][::-1]
        return ans


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
