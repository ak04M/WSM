from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)

    def add_document(self, doc_id, tokens):
        unique_tokens = set(tokens)

        for token in unique_tokens:
            if doc_id not in self.index[token]:
                self.index[token].append(doc_id)

    def build(self, documents):
        for doc_id, tokens in documents.items():
            self.add_document(doc_id, tokens)

        for token in self.index:
            self.index[token].sort()

    def get_postings(self, term):
        return self.index.get(term, [])

    def get_dictionary(self):
        return sorted(self.index.keys())

    def __contains__(self, term):
        return term in self.index