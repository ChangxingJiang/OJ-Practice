from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]}

        ans = [""]
        for d in digits:
            if d in phone:
                new = []
                for item in ans:
                    for c in phone[d]:
                        new.append(item + c)
                ans = new

        return ans


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    print(Solution().letterCombinations(""))  # [].
