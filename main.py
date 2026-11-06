from src.document_loader import load_documents
from src.tokenizer import tokenize
from src.normalizer import normalize_tokens
from src.inverted_index import InvertedIndex
from src.query_processor import QueryProcessor
from src.wildcard_processor import PermutermIndex, wildcard_search
from src.gui import SearchGUI


def main():
    documents, filenames = load_documents("data/documents")

    print(f"Loaded {len(documents)} documents.")

    processed_documents = {}

    for doc_id, text in documents.items():
        tokens = tokenize(text)
        normalized_tokens = normalize_tokens(tokens)

        processed_documents[doc_id] = normalized_tokens

    inverted_index = InvertedIndex()
    inverted_index.build(processed_documents)

    print(
        f"Indexed {len(inverted_index.get_dictionary())} unique terms."
    )

    query_processor = QueryProcessor(
        inverted_index,
        len(documents)
    )

    permuterm_index = PermutermIndex()

    permuterm_index.build(
        inverted_index.get_dictionary()
    )

    def process_wildcard_query(query):
        return wildcard_search(
            query.lower(),
            permuterm_index,
            inverted_index
        )

    app = SearchGUI(
        query_processor,
        process_wildcard_query,
        filenames
    )

    app.run()


if __name__ == "__main__":
    main()