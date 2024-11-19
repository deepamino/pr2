from processing.Aligner import *

class AlignerArgs:
    def __init__(
                self,
                match_score=1.0,
                mismatch_score=0.0,
                target_internal_open_gap_score=0.0,
                target_internal_extend_gap_score=0.0,
                target_left_open_gap_score=0.0,
                target_left_extend_gap_score=0.0,
                target_right_open_gap_score=0.0,
                target_right_extend_gap_score=0.0,
                query_internal_open_gap_score=0.0,
                query_internal_extend_gap_score=0.0,
                query_left_open_gap_score=0.0,
                query_left_extend_gap_score=0.0,
                query_right_open_gap_score=0.0,
                query_right_extend_gap_score=0.0,
            ):

        self.match_score = match_score
        self.mismatch_score = mismatch_score
        self.target_internal_open_gap_score = target_internal_open_gap_score
        self.target_internal_extend_gap_score = target_internal_extend_gap_score
        self.target_left_open_gap_score = target_left_open_gap_score
        self.target_left_extend_gap_score = target_left_extend_gap_score
        self.target_right_open_gap_score = target_right_open_gap_score
        self.target_right_extend_gap_score = target_right_extend_gap_score
        self.query_internal_open_gap_score = query_internal_open_gap_score
        self.query_internal_extend_gap_score = query_internal_extend_gap_score
        self.query_left_open_gap_score = query_left_open_gap_score
        self.query_left_extend_gap_score = query_left_extend_gap_score
        self.query_right_open_gap_score = query_right_open_gap_score
        self.query_right_extend_gap_score = query_right_extend_gap_score

    def __str__(self):
        return f"""AlignerArgs(match_score={self.match_score}, 
                    mismatch_score={self.mismatch_score}, 
                    target_internal_open_gap_score={self.target_internal_open_gap_score}, 
                    target_internal_extend_gap_score={self.target_internal_extend_gap_score}, 
                    target_left_open_gap_score={self.target_left_open_gap_score}, 
                    target_left_extend_gap_score={self.target_left_extend_gap_score}, 
                    target_right_open_gap_score={self.target_right_open_gap_score}, 
                    target_right_extend_gap_score={self.target_right_extend_gap_score}, 
                    query_internal_open_gap_score={self.query_internal_open_gap_score}, 
                    query_internal_extend_gap_score={self.query_internal_extend_gap_score}, 
                    query_left_open_gap_score={self.query_left_open_gap_score}, 
                    query_left_extend_gap_score={self.query_left_extend_gap_score}, 
                    query_right_open_gap_score={self.query_right_open_gap_score}, 
                    query_right_extend_gap_score={self.query_right_extend_gap_score})"""



class AlignerBuilder:
    def __init__(self):
        self.aligner = PairwiseAligner()

    def with_args(self, args: AlignerArgs):
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

    def build(self):
        return self.aligner