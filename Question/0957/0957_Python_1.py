from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        count = {"".join(str(c) for c in cells): 0}
        lst = [cells]
        i = 0
        while True:
            i += 1

            # 计算调换
            new = [0] * 8
            for j in range(1, 7):
                if cells[j - 1] == cells[j + 1]:
                    new[j] = 1
                else:
                    new[j] = 0
            cells = new
            lst.append(cells)

            s = "".join(str(c) for c in cells)

            if s in count:
                start = count[s]
                circle = i - count[s]  # 循环周期
                break
            else:
                count[s] = i

        return lst[(N - start) % circle + start]


if __name__ == "__main__":
    # [0,0,1,1,0,0,0,0]
    print(Solution().prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7))

    # [0,0,1,0,0,1,0,0]
    print(Solution().prisonAfterNDays(cells=[1, 1, 0, 1, 1, 0, 1, 1], N=6))

    # [0,0,1,1,1,1,0,0]
    print(Solution().prisonAfterNDays(cells=[1, 1, 0, 0, 0, 0, 1, 1], N=7))

    # [0,0,1,1,1,1,1,0]
    print(Solution().prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))
