from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(log):
            id_, content = log.split(" ", 1)
            return (0, content, id_) if content[0].isalpha() else (1,)

        return sorted(logs, key=helper)


if __name__ == "__main__":
    print(Solution().reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
    # ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
