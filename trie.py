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
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True


if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "banana", "bat", "ball"]
    for word in words:
        trie.insert(word)
    print("Inserted words into trie.")

    trie.print(trie.root)

    tests = {
        "ban": {"method": trie.starts_with, "args": ("ban",)},
        "bon": {"method": trie.starts_with, "args": ("bon",)},
        "banan": {"method": trie.starts_with, "args": ("banan",)},
    }
    for name, test in tests.items():
        args = test.get("args", ())        # Get positional args, default to empty tuple
        kwargs = test.get("kwargs", {})    # Get keyword args, default to empty dict
        result = test["method"](*args, **kwargs)  # Unpack both args and kwargs
        print(f"{name}: {result}")
        print("---------")
    

