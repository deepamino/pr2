import Bio.Align as Align
from Bio.Align import substitution_matrices

from abc import ABC, abstractmethod


class Aligner(ABC):
    @abstractmethod
    def align(self, seq1, seq2, *args):
        pass


class PairwiseAligner(Aligner):
    def __init__(self):
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'global'

    def align(self, seq1, seq2, matrix=None):
        if matrix is not None:
            self.aligner.substitution_matrix = substitution_matrices.load(matrix)
            
        alignment = self.aligner.align(seq1, seq2)
        return alignment
