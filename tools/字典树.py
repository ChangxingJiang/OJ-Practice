def build_tree(words):
    tree = {}
    for i, word in enumerate(words):
        node = tree
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["@"] = i