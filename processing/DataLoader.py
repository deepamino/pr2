import random
import os

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

        self.get_sequences_by_id(id_list)
        return sequences
    
    def get_sequences_by_id(self, ids, db="protein", folder="sequences"):
        routes = []
        for id in ids:
            with Entrez.efetch(db=db, id=id, rettype="fasta", retmode="text") as fetch:
                content = fetch.read()
            
            first_line = content.split("\n")[0]
            unique_id = first_line.split()[0][1:]
            filename = unique_id.replace(".", "_") + ".fasta"
            file_route = os.path.join(folder, filename)
            
            with open(file_route, "w") as file:
                file.write(content)
                print(f"File {filename} created")

            routes.append(file_route)
        
        return routes


class DataLoaderFactory:
    @staticmethod
    def get_loader(loader_type):
        if loader_type == "random":
            return RandomSequenceLoader()
        
        elif loader_type == "api":
            return ApiSequenceLoader()