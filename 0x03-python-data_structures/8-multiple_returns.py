#!/usr/bin/python3
def multiple_returns(sentence):
    """
    multiple_returns - Get tuple of the length of string and first character
    @sentence: The string want to get his len and first char
    Return: Tuple (length, first character)
    """
    sLen = len(sentence)
    return (sLen, sentence[0] if sLen > 0 else None)
