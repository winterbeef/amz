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





if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "banana", "bat", "ball"]
    for word in words:
        trie.insert(word)
    print("Inserted words into trie.")

    trie.print(trie.root)
    

