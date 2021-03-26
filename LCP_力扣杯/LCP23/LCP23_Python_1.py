from typing import List


class Solution:
    def isMagic(self, target: List[int]) -> bool:
        n = len(target)

        # 生成初始状态
        cards = [i for i in range(2, n + 1, 2)] + [i for i in range(1, n + 1, 2)]

        # 计算k值
        k = 0
        for j in range(n):
            if cards[j] == target[j]:
                k += 1
            else:
                break

        if k == 0:
            return False

        if k == n:
            return True

        # 情景模拟
        i = k
        while i < n:
            change = [cards[j] for j in range(k + 1, n - i + k, 2)] + [cards[j] for j in range(k, n - i + k, 2)]
            # print(cards, "->", change)
            for j in range(min(k, n - i)):
                if change[j] != target[i + j]:
                    return False
            cards = change
            i += k

        return True


if __name__ == "__main__":
    # True
    print(Solution().isMagic([2, 4, 3, 1, 5]))

    # False
    print(Solution().isMagic([5, 4, 3, 2, 1]))

    # True
    print(Solution().isMagic(
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27,
         29, 31, 33]))
