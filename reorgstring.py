#!/usr/bin/env python

# from typing import List
import heapq

def reorganizeString(s: str) -> str:
    # Build frequency histogram
    hist = {}
    for c in s:
        if c not in hist:
            hist[c] = 0
        hist[c] += 1

    # Build max-heap based on frequencies
    heap = []
    for (c, freq) in hist.items():
        heapq.heappush(heap, (-freq, c))

    word = []
    lastc = ""

    # Reorganize string
    while heap:
        # Pop the most frequent character
        (negfreq, c) = heapq.heappop(heap)

        # If it's the same as the last character used, try the next most frequent
        if c == lastc:
            if heap:
                # Get the next most frequent character
                (negfreq2, c2) = heapq.heappop(heap)
                heapq.heappush(heap, (negfreq, c))
                (negfreq, c) = (negfreq2, c2)
            else:
                return ""
            
        # Append the chosen character to the result
        word.append(c)
        lastc = c

        # Decrease frequency and push back if still available
        negfreq += 1
        if negfreq < 0:
            heapq.heappush(heap, (negfreq, c))
            
    return "".join(word)



if __name__ == "__main__":
    s = "aaabffbbecaaaaaceeeeghghghaqcw"
    so = reorganizeString(s)
    print(so)