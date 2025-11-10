#!/usr/bin/env python3
"""

"""

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )    
    parser.add_argument(
        "-s", "--string",
        type=str,
        help="Input string to reverse"
    )    
    args = parser.parse_args()
    print(reverseit(s=args.string, verbose=args.verbose))




def reverseit(s="", verbose=False):
    if verbose:
        print("processing")

    if len(s) < 2:
        return s
    else:
        return reverseit(s[1:])+s[0]



if __name__ == "__main__":
    main()


