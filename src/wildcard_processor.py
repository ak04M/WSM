class PermutermIndex:
    def __init__(self):
        self.index = {}

    def add_term(self, term):
        word = term + "$"

        for i in range(len(word)):
            rotation = word[i:] + word[:i]
            self.index[rotation] = term

    def build(self, dictionary):
        for term in dictionary:
            self.add_term(term)

    def get_matching_terms(self, wildcard_query):
        if "*" not in wildcard_query:
            return [wildcard_query]

        parts = wildcard_query.split("*")

        before = parts[0]
        after = parts[1]

        prefix = after + "$" + before

        matching_terms = set()

        for rotation, original_term in self.index.items():
            if rotation.startswith(prefix):
                matching_terms.add(original_term)

        return sorted(matching_terms)


def wildcard_search(wildcard_query, permuterm_index, inverted_index):
    matching_terms = permuterm_index.get_matching_terms(
        wildcard_query
    )

    result = set()

    for term in matching_terms:
        postings = inverted_index.get_postings(term)
        result.update(postings)

    return sorted(result)