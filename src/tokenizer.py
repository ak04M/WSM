import re


def tokenize(text):
    tokens = re.findall(r"[A-Za-z0-9]+", text)

    return tokens