import random
from Bio.Align import PairwiseAligner
from Bio.Align import substitution_matrices
from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Entrez

from abc import ABC, abstractmethod


class DataLoader(ABC):
    @abstractmethod
    def load(self):
        pass


class RandomSequenceLoader(DataLoader):
    def __init__(self):
        self.alphabet = "ACDEFGHIKLMNPQRSTVWY"

    def load(self, length):
        return Seq(''.join(random.choices(self.alphabet, k=length)))
    

class ApiSequenceLoader(DataLoader):
    def __init__(self):
        self.email = 'example@gmail.com'
        self.type = 'protein'
        Entrez.email = self.email

    def load(self, id_list):
        ids = ",".join(id_list)
        handle = Entrez.efetch(db=self.type, id=ids, rettype="fasta", retmode="text")
        sequences = list(SeqIO.parse(handle, "fasta"))
        handle.close()

        return sequences

    def search_protein(self, term, retmax=10):
        handle = Entrez.esearch(db=self.type, term=term, retmax=retmax)
        record = Entrez.read(handle)
        handle.close()

        id_list = record["IdList"]
        print(f"Found {len(id_list)} results.")
        return id_list
    

class DataLoaderFactory:
    @staticmethod
    def get_loader(loader_type):
        if loader_type == "random":
            return RandomSequenceLoader()
        
        elif loader_type == "api":
            return ApiSequenceLoader()