"""
题目格式整理工具

题目列表Url：https://leetcode-cn.com/api/problems/all/
题目翻译Url：https://leetcode-cn.com/graphql
题目标签Url：https://leetcode-cn.com/problems/api/tags/
题目类型Url：https://leetcode-cn.com/problems/api/favorites/
"""

import json


def arrange_problem():
    """
    解析“题目列表”
    解析内容：题目ID、题目前端ID、题目Url、题目难度、题目是否付费(✖)

    :return: <dict>
    """
    with open("题目列表(20200617).json", "r")as file:
        question_dict = json.loads(file.read())

    question_result = {}
    for question_item in question_dict["stat_status_pairs"][::-1]:
        # 提取题目ID
        question_id = question_item["stat"]["question_id"]

        # 提取题目编号
        num = question_item["stat"]["frontend_question_id"]
        num = num.zfill(4)

        # 提取题目名称
        title = question_item["stat"]["question__title"]

        # 提取题目Url
        title = question_item["stat"]["question__title"]  # 题目标题
        url = "https://leetcode-cn.com/problems/" + question_item["stat"]["question__title_slug"] + "/"

        # 提取题目难度
        level = question_item["difficulty"]["level"]
        if level == 1:
            level_name = "简单"
        elif level == 2:
            level_name = "中等"
        elif level == 3:
            level_name = "困难"
        else:
            level_name = str(level)

        # 提取题目是否付费
        paid = question_item["paid_only"]

        question_result[num] = {
            "id": question_id,
            "title": title,
            "url": url,
            "level": level_name,
            "paid": paid
        }

    return question_result


def arrange_translate():
    """
    解析“题目翻译”
    解析内容：题目ID、题目中文标题

    :return: <dict>
    """
    with open("题目翻译(20200618).json", "r")as file:
        question_dict = json.loads(file.read())

    question_result = {}
    for question_item in question_dict["data"]["translations"]:
        question_result[question_item["questionId"].zfill(4)] = question_item["title"]
    return question_result


def arrange_label():
    """
    解析“题目标签”
    解析内容：题目ID、题目对应标签

    :return: <dict>
    """
    with open("题目标签(20200617).json", "r", encoding="UTF-8")as file:
        question_dict = json.loads(file.read())

    question_result = {}
    for question_item in question_dict["topics"]:
        name = question_item["translatedName"]
        for question_id in question_item["questions"]:
            if question_id not in question_result:
                if name:
                    question_result[question_id] = [name]
            else:
                if name:
                    question_result[question_id].append(name)
    return question_result


if __name__ == "__main__":
    problems = arrange_problem()
    translates = arrange_translate()
    labels = arrange_label()

    for num in problems:

    # for i in range(1, 1486):
    #     num = str(i).zfill(4)  # 题目编号
    #     if num not in problems:
    #         continue

        title = problems[num]["title"]
        url = problems[num]["url"]
        level = problems[num]["level"]
        paid = problems[num]["paid"]

        if paid:
            paid = "会员"
        else:
            paid = "免费"

        id = problems[num]["id"]
        if num in translates:
            title = translates[num]

        label = ""
        if id in labels:
            label = ",".join(labels[id])

        print("\t".join([num, title, url, level, label, paid]))
