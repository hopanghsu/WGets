#!/usr/bin/python3

import sys
import subprocess

def walk(tokens, pos, prefix_path, prefix_name):
    #
    if pos == len(tokens):
        if subprocess.run(["wget", prefix_path,
                           "-O", prefix_name]).returncode != 0:
           subprocess.run(["rm", prefix_name])
           return False

        return True

    #
    if tokens[pos] != "<3D>":
        return walk(tokens,
                    pos + 1,
                    prefix_path + tokens[pos],
                    prefix_name)

    #
    for i in range(1, 1000):
        n = str(i).zfill(3)
        if not walk(tokens,
                    pos + 1,
                    prefix_path + n,
                    prefix_name + "-" + n):
            # If we fail to fetch the very first node,
            # then we can give up the entire sub-tree.
            return False if i == 1 else True

    #
    return True

def wgets(name, pattern):
    walk(pattern.split("\'"), 0, "", name)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise NameError("Please enter a valid name and a valid pattern"
                        "for deriving the download targets.")

    wgets("downloads/" + sys.argv[1], sys.argv[2])

