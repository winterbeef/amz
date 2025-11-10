#!/usr/bin/env python

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_word = False

# def wordBreakTrie(s, wordDict):
#     # Build Trie
#     root = TrieNode()
#     for word in wordDict:
#         node = root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_word = True
    
#     result = []
    
#     def backtrack(start, path):
#         if start == len(s):
#             result.append(' '.join(path))
#             return
        
#         node = root
#         for end in range(start, len(s)):
#             char = s[end]
#             if char not in node.children:
#                 break
#             node = node.children[char]
#             if node.is_word:
#                 backtrack(end + 1, path + [s[start:end + 1]])
    
#     backtrack(0, [])
#     return result

def wordBreak(s, wordDict):
    word_set = set(wordDict)
    memo = {}
    
    def backtrack(start):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [[]]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                # Get all valid segmentations for remaining string
                sub_results = backtrack(end)
                for sub_result in sub_results:
                    result.append([word] + sub_result)
        
        memo[start] = result
        return result
    
    return [' '.join(words) for words in backtrack(0)]

if __name__ == "__main__":
    s = "catsanddog"
    words = ["cat","cats","and","sand","dog"]

    result = wordBreak(s, words)
    print(result)