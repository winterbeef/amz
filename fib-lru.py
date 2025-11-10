#!/usr/bin/env python

import functools

@functools.lru_cache()
def fib(nth):
    """Return the nth Fibonacci number using memoization."""
    if nth == 0:
        return 0
    elif nth == 1:
        return 1
    else:
        return fib(nth - 1) + fib(nth - 2)


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 fib.py <nth>")
        sys.exit(1)
    try:
        nth = int(sys.argv[1])
        if nth < 0:
            raise ValueError
    except ValueError:
        print("Please provide a non-negative integer for <nth>.")
        sys.exit(1)
    
    print(f"The {nth}th Fibonacci number is: {fib(nth)}")