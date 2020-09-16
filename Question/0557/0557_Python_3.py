class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        ans = []
        for i in range(len(n)):
            ans.append(n[i][::-1])
        return " ".join(ans)


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
