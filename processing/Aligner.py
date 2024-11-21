import Bio.Align as Align
from Bio.Align import substitution_matrices

from abc import ABC, abstractmethod

from processing.AlignerArgs import AlignerArgs


class Aligner(ABC):
    @abstractmethod
    def align(self, seq1, seq2, *args):
        pass


class PairwiseAligner(Aligner):
    def __init__(self):
        self.aligner = Align.PairwiseAligner()
        self.aligner.mode = 'local'

    def align(self, seq1, seq2, matrix=None):
        if matrix is not None:
            self.aligner.substitution_matrix = substitution_matrices.load(matrix)

        alignment = self.aligner.align(seq1, seq2)
        return alignment
    
    def from_args(self, args):
        self.aligner.match_score = args.match_score
        self.aligner.mismatch_score = args.mismatch_score
        self.aligner.target_internal_open_gap_score = args.target_internal_open_gap_score
        self.aligner.target_internal_extend_gap_score = args.target_internal_extend_gap_score
        self.aligner.target_left_open_gap_score = args.target_left_open_gap_score
        self.aligner.target_left_extend_gap_score = args.target_left_extend_gap_score
        self.aligner.target_right_open_gap_score = args.target_right_open_gap_score
        self.aligner.target_right_extend_gap_score = args.target_right_extend_gap_score
        self.aligner.query_internal_open_gap_score = args.query_internal_open_gap_score
        self.aligner.query_internal_extend_gap_score = args.query_internal_extend_gap_score
        self.aligner.query_left_open_gap_score = args.query_left_open_gap_score
        self.aligner.query_left_extend_gap_score = args.query_left_extend_gap_score
        self.aligner.query_right_open_gap_score = args.query_right_open_gap_score
        self.aligner.query_right_extend_gap_score = args.query_right_extend_gap_score

        return self
    
    def args(self):
        return AlignerArgs(
            match_score=self.aligner.match_score,
            mismatch_score=self.aligner.mismatch_score,
            target_internal_open_gap_score=self.aligner.target_internal_open_gap_score,
            target_internal_extend_gap_score=self.aligner.target_internal_extend_gap_score,
            target_left_open_gap_score=self.aligner.target_left_open_gap_score,
            target_left_extend_gap_score=self.aligner.target_left_extend_gap_score,
            target_right_open_gap_score=self.aligner.target_right_open_gap_score,
            target_right_extend_gap_score=self.aligner.target_right_extend_gap_score,
            query_internal_open_gap_score=self.aligner.query_internal_open_gap_score,
            query_internal_extend_gap_score=self.aligner.query_internal_extend_gap_score,
            query_left_open_gap_score=self.aligner.query_left_open_gap_score,
            query_left_extend_gap_score=self.aligner.query_left_extend_gap_score,
            query_right_open_gap_score=self.aligner.query_right_open_gap_score,
            query_right_extend_gap_score=self.aligner.query_right_extend_gap_score,
        )

