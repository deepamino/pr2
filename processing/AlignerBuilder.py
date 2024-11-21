from processing.Aligner import *


class AlignerBuilder:
    def __init__(self):
        self.aligner = PairwiseAligner()

    def build(self, args=None):
        if args is not None:
            return self.aligner.from_args(args)

        return self.aligner