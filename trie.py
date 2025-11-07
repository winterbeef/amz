#!/usr/bin/env python

class Node(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_end = True

    def print(self, node):
        for c, n in node.children.items():
            print(c)
            self.print(node=n)

    def starts_with(self, prefix):
        words = []
        current_node = self.root

        # 1. Get to the node matched by 'prefix'
        for c in prefix:
            if c not in current_node.children:
                return words
            current_node = current_node.children[c]

        # 2. From there, a recursive DFS collecting words. The closure makes 'words' visible
        def _dfs(current_node, path):
            if current_node.is_end:
                words.append(''.join(path))
            for c, child_node in current_node.children.items():
                _dfs(child_node, path + [c])

        _dfs(current_node, list(prefix))

        return words

    def list_words(self):
        words = []

        def _dfs(current_node, path):
            if current_node.is_end:
                words.append(''.join(path))
            for c, child_node in current_node.children.items():
                _dfs(child_node, path + [c])

        _dfs(self.root, [])

        return words


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "banana", "bat", "ball", "batten", "battery"]
    for word in words:
        trie.insert(word)
    print("Inserted words into trie.")

    trie.print(trie.root)
    words = trie.starts_with('bat')
    print(f"'bat': {words}")

    allwords = trie.list_words()
    print(f"ALL: {allwords}")
