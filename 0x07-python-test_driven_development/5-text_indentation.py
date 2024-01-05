#!/usr/bin/python3
"""
5-text_indentation.py - print a betty text module
"""


def text_indentation(text):
    """
    text_indentation - print betty text

    Args:
        text (string): the text to print
    Raises:
        TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = 0
    for c in text:
        if c != " ":
            break
        s += 1

    nl = False
    for c in text[s:]:
        if nl and c == " ":
            continue
        print(c, end="")
        if c == "\n" or c in ".?:":
            if c in ".?:":
                print("\n")
            nl = True
