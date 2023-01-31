#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    firstChar = sentence[0] if len(sentence) > 0 else None
    return (strlen, firstChar)
