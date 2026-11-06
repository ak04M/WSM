def normalize_token(token):
    return token.lower()


def normalize_tokens(tokens):
    return [normalize_token(token) for token in tokens]