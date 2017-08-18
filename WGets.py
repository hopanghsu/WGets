#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NameError("Please enter a valid pattern"
                        "for deriving the download targets.")

    print(sys.argv[1])

