#!/usr/bin/env python

from typing import List

class Solution:
        def minimumOperations(self, nums: List[int]) -> int:
            pass
    
def doit(nums):
        nonzero = list(filter(lambda n: n>0, nums))
        tries = 0
        while nonzero:
                smallest = min(nonzero)
                nums = [max(0, n-smallest) for n in nums]
                nonzero = list(filter(lambda n: n>0, nums))
                print(nums)
                tries += 1
        return tries


if __name__ == "__main__":
    nums = [1,15,0,13,5]
    print(f"Start: {nums}")
    tries = doit(nums)
    print(f"tries: {tries}")
