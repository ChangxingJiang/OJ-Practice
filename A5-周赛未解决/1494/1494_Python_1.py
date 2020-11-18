from typing import List


class Node:
    def __init__(self, i):
        self.i = i
        self.need = []


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        # 整理依赖关系
        courses = [Node(i) for i in range(1, n + 1)]
        independent_courses = {i for i in range(1, n + 1)}  # 没有依赖的课程
        hardest_courses = {i for i in range(1, n + 1)}  # 需要条件最高的课程
        for dependency in dependencies:
            courses[dependency[1] - 1].need.append(courses[dependency[0] - 1])

            if dependency[0] in hardest_courses:
                hardest_courses.remove(dependency[0])
            if dependency[0] in independent_courses:
                independent_courses.remove(dependency[0])
            if dependency[1] in independent_courses:
                independent_courses.remove(dependency[1])

        hardest_courses -= independent_courses

        # 计算每一个课程体系的各个层级的课程列表
        level_courses_list_for_systems = []
        for course in hardest_courses:
            level_courses_list = [{course}]
            while True:
                now_level_courses = level_courses_list[-1]
                next_level_courses = set()
                for course2 in list(now_level_courses):
                    for easier_course in courses[course2 - 1].need:
                        next_level_courses.add(easier_course.i)
                        if easier_course.i in level_courses_list[-1]:
                            level_courses_list[-1].remove(easier_course.i)
                # print("当前各层课程列表:", level_courses_list)
                if not next_level_courses:
                    break
                else:
                    level_courses_list.append(next_level_courses)

            # 计算各个层级的课程数量
            level_courses_num = []
            for level_courses in level_courses_list:
                if level_courses:
                    level_courses_num.append(len(level_courses))

            level_courses_list_for_systems.append(level_courses_num)

        # 计算不需要依赖的课程数量
        other_courses_num = len(independent_courses)

        print(other_courses_num, level_courses_list_for_systems)

        # 计算总共需要的学期数
        # ans = 0
        # already_learned_num = 0
        # while already_learned_num < n:
        #     ans += 1
        #     if len(level_courses_num) > 0:
        #         if level_courses_num[-1] > k:
        #             level_courses_num[-1] -= k
        #             already_learned_num += k
        #         else:
        #             num = level_courses_num.pop()
        #             already_learned_num += num
        #             if other_courses_num:
        #                 other = k - num
        #                 if other:
        #                     if other > other_courses_num:
        #                         other_courses_num -= other
        #                         already_learned_num += other
        #                     else:
        #                         already_learned_num += other_courses_num
        #                         other_courses_num = 0
        #     else:
        #         other_courses_num -= k
        #         if other_courses_num <= 0:
        #             return ans

            # print(ans, ":", other_courses_num, level_courses_num)

        # return ans


if __name__ == "__main__":
    # 3
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[2, 1], [3, 1], [1, 4]], k=2))

    # 4
    print(Solution().minNumberOfSemesters(n=5, dependencies=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2))

    # 6
    print(Solution().minNumberOfSemesters(n=11, dependencies=[], k=2))

    # 5
    print(Solution().minNumberOfSemesters(
        n=5,
        dependencies=[[1, 5], [1, 3], [1, 2], [4, 2], [4, 5], [2, 5], [1, 4], [4, 3], [3, 5], [3, 2]], k=3))

    # 4
    print(Solution().minNumberOfSemesters(n=4, dependencies=[[1, 2], [4, 2]], k=1))

    # 6
    print(Solution().minNumberOfSemesters(n=12,
                                          dependencies=[[1, 2], [1, 3], [7, 5], [7, 6], [4, 8], [8, 9], [9, 10],
                                                        [10, 11], [11, 12]],
                                          k=2))
