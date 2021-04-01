class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ans = [""]
        for ch in word:
            if ch.isdigit():
                ans[-1] += ch
            else:
                ans.append("")
        return len({int(num) for num in ans if num != ""})


if __name__ == "__main__":
    print(Solution().numDifferentIntegers("a123bc34d8ef34"))  # 3
    print(Solution().numDifferentIntegers("leet1234code234"))  # 2
    print(Solution().numDifferentIntegers("a1b01c001"))  # 1
