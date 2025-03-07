import os
import pickle

from core.parser import parse_file


class Indexer:
    def __init__(self, docs_dir):
        self.docs_dir = docs_dir
        self.index = {}

    def build(self):
        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                filepath = os.path.join(root, file)
                words = parse_file(filepath)
                for word in set(words):
                    self.index.setdefault(word, []).append(filepath)

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.index, f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.index = pickle.load(f)
