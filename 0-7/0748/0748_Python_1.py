from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().shortestCompletingWord(licensePlate="1s3 PSt",
                                            words=["step", "steps", "stripe", "stepple"]))  # steps
    print(Solution().shortestCompletingWord(licensePlate="1s3 456", words=["looks", "pest", "stew", "show"]))  # pest
