import random
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices

from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load(self):
        pass


class RandomSequenceLoader(DataLoader):
    def __init__(self):
        self.alphabet = "ACDEFGHIKLMNPQRSTVWY"

    def load(self, length):
        return ''.join(random.choices(self.alphabet, k=length))
    

class DataLoaderFactory:
    @staticmethod
    def get_loader(loader_type):
        if loader_type == "random":
            return RandomSequenceLoader()
        else:
            raise ValueError("Unknown loader type")