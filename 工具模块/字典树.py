def build_tree(words):
    tree = {}
    for i, word in enumerate(words):
        node = tree
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["@"] = i
    return tree


# 字典树匹配位置
def use_tree(text, tree):
    ans = []
    for i in range(len(text)):
        node = tree
        j = i
        while j < len(text) and text[j] in node:
            node = node[text[j]]
            if "@" in node:
                ans.append([i, j])
            j += 1
    return ans
