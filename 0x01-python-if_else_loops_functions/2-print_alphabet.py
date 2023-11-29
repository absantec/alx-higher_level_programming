#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""
for s in range(97, 123):
    print(chr(s).format(), end="")
