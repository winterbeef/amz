#!/usr/bin/env python3
"""
Template for a Python script.
"""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Template for a Python script.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "input_file",
        type=Path,
        help="Input file path"
    )
    
    parser.add_argument(
        "-o", "--output",
        type=Path,
        help="Output file path (optional)"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not args.input_file.exists():
        print(f"Error: Input file '{args.input_file}' not found", file=sys.stderr)
        sys.exit(1)
    
    if args.verbose:
        print(f"Processing file: {args.input_file}")
    
    process_file(args.input_file, args.output, args.verbose)


def process_file(input_path, output_path=None, verbose=False):
    if verbose:
        print(f"Reading from: {input_path}")
    
    try:
        with open(input_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(content)
            if verbose:
                print(f"Output written to: {output_path}")
        else:
            print(content)
            
    except IOError as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()