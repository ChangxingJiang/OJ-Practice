class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split(" ")
        for i in range(len(n)):
            n[i] = n[i][::-1]
        return " ".join(n)


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
