class SearchEngine:
    def __init__(self, index):
        self.index = index

    def search(self, query):
        return self.index.get(query.lower(), [])