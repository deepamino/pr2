import seaborn as sns
import matplotlib.pyplot as plt

import numpy as np


class Visualizer:
    def __init__(self):
        pass

    def plot_alignment_matrix(target, query, match_line):
        matrix = np.zeros((len(query), len(target)))

        for i, (q, t, m) in enumerate(zip(query, target, match_line)):
            if m == "|":
                matrix[i, i] = 1

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.matshow(matrix, cmap="Blues", alpha=0.5)

        for i in range(len(query)):
            for j in range(len(target)):
                if i == j:
                    ax.text(j, i, query[i], va='center', ha='center', fontsize=10, color="black")
                else:
                    ax.text(j, i, ".", va='center', ha='center', fontsize=10, color="black")

        ax.set_xticks(range(len(target)))
        ax.set_xticklabels(list(target), fontsize=10, rotation=90)
        ax.set_yticks(range(len(query)))
        ax.set_yticklabels(list(query), fontsize=10)

        ax.set_xlabel("Target Sequence", fontsize=12)
        ax.set_ylabel("Query Sequence", fontsize=12)
        plt.title("Alignment Matrix", fontsize=14)
        plt.show()