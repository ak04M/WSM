class QueryProcessor:
    def __init__(self, inverted_index, total_documents):
        self.inverted_index = inverted_index
        self.total_documents = total_documents

    def and_operation(self, list1, list2):
        result = []

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):

            if list1[i] == list2[j]:
                result.append(list1[i])
                i += 1
                j += 1

            elif list1[i] < list2[j]:
                i += 1

            else:
                j += 1

        return result

    def or_operation(self, list1, list2):
        result = []

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):

            if list1[i] == list2[j]:
                result.append(list1[i])
                i += 1
                j += 1

            elif list1[i] < list2[j]:
                result.append(list1[i])
                i += 1

            else:
                result.append(list2[j])
                j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])

        return result

    def not_operation(self, postings):
        all_documents = set(range(1, self.total_documents + 1))

        return sorted(all_documents - set(postings))

    def search_term(self, term):
        return self.inverted_index.get_postings(term)

    def search(self, query):
        query = query.strip()

        parts = query.split()

        if len(parts) == 1:
            term = parts[0].lower()
            return self.search_term(term)

        if len(parts) != 3:
            return []

        term1 = parts[0].lower()
        operator = parts[1].upper()
        term2 = parts[2].lower()

        postings1 = self.search_term(term1)
        postings2 = self.search_term(term2)

        if operator == "AND":
            return self.and_operation(postings1, postings2)

        elif operator == "OR":
            return self.or_operation(postings1, postings2)

        elif operator == "NOT":
            return self.and_operation(
                postings1,
                self.not_operation(postings2)
            )

        return []