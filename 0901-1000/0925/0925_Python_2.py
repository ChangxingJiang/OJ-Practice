import itertools


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1 = [(k, len(list(group))) for k, group in itertools.groupby(name)]
        g2 = [(k, len(list(group))) for k, group in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False
        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))


if __name__ == "__main__":
    print(Solution().isLongPressedName("alex", "aaleex"))  # True
    print(Solution().isLongPressedName("saeed", "ssaaedd"))  # False
    print(Solution().isLongPressedName("leelee", "lleeelee"))  # True
    print(Solution().isLongPressedName("laiden", "laiden"))  # True
    print(Solution().isLongPressedName("vtkgn", "vtkgnn"))  # True
