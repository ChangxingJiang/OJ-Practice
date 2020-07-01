from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        patterns = list(filter(str.isalpha, licensePlate.lower()))
        ans = " " * 15
        for word in words:
            alpha = list(word)
            for p in patterns:
                if p not in alpha:
                    break
                alpha.remove(p)
            else:
                if len(word) < len(ans):
                    ans = word
        return ans


if __name__ == "__main__":
    print(Solution().shortestCompletingWord(licensePlate="1s3 PSt",
                                            words=["step", "steps", "stripe", "stepple"]))  # steps
    print(Solution().shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]))  # pest
