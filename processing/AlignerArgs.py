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