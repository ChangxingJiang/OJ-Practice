from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])

        old_color = image[sr][sc]

        aim_list = []
        now_aim_list = [(sr, sc)]
        while len(now_aim_list) > 0:
            aim_list.extend(now_aim_list)
            new_aim_list = []
            for (r, c) in now_aim_list:
                if r > 0 and image[r - 1][c] == old_color:
                    if (r - 1, c) not in aim_list and (r - 1, c) not in new_aim_list:
                        new_aim_list.append((r - 1, c))
                if c > 0 and image[r][c - 1] == old_color:
                    if (r, c - 1) not in aim_list and (r, c - 1) not in new_aim_list:
                        new_aim_list.append((r, c - 1))
                if r < h - 1 and image[r + 1][c] == old_color:
                    if (r + 1, c) not in aim_list and (r + 1, c) not in new_aim_list:
                        new_aim_list.append((r + 1, c))
                if c < w - 1 and image[r][c + 1] == old_color:
                    if (r, c + 1) not in aim_list and (r, c + 1) not in new_aim_list:
                        new_aim_list.append((r, c + 1))
            now_aim_list = new_aim_list

        for (r, c) in aim_list:
            image[r][c] = newColor

        return image


if __name__ == "__main__":
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]
