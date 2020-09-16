from typing import List


class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        new_indexes = sorted([(indexes[i], i) for i in range(len(indexes))], key=lambda k: k[0])
        idx_change = 0  # 坐标变化
        for i in range(len(new_indexes)):
            index = new_indexes[i]
            idx = index[0] + idx_change
            n1 = len(sources[index[1]])
            n2 = len(targets[index[1]])
            if S[idx:idx + n1] == sources[index[1]]:
                S = S[:idx] + targets[index[1]] + S[idx + n1:]
                idx_change += n2 - n1
        return S


if __name__ == "__main__":
    print(Solution().findReplaceString(S="abcd", indexes=[0, 2], sources=["a", "cd"], targets=["eee", "ffff"]))  # "eeebffff"
    print(Solution().findReplaceString(S="abcd", indexes=[0, 2], sources=["ab", "ec"], targets=["eee", "ffff"]))  # "eeecd"
    print(Solution().findReplaceString(S="vmokgggqzp", indexes=[3, 5, 1], sources=["kg", "ggq", "mo"], targets=["s", "so", "bfr"]))  # "vbfrssozp"
