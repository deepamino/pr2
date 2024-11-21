import random
import copy

from processing.AlignerBuilder import *


class GeneticAlgorithm:
    def __init__(self, population_size, max_generations, sequence1, sequence2, fitness_function):
        self.population_size = population_size
        self.max_generations = max_generations
        self.sequence1 = sequence1
        self.sequence2 = sequence2
        self.fitness_function = fitness_function

    def run(self, target, query):
        pass
    
    def crossover(self, parent1, parent2):
        child = copy.deepcopy(parent1)
        parent1_args = parent1.args()
        parent2_args = parent2.args()

        for key in parent1_args.__dict__:
            if random.random() < 0.5:
                setattr(child, key, getattr(parent2_args, key))

        return child
        
    def mutate(self, individual):
        individual_args = individual.args()
        for key in individual_args.__dict__:
            if random.random() < 0.1:
                setattr(individual, key, random.random())
        return individual

    def generate_individual(self):
        args = AlignerArgs(
            match_score=random.random()*10,
            mismatch_score=random.random()*(-10),
            target_internal_open_gap_score=random.random()*(-10),
            target_internal_extend_gap_score=random.random()*(-10),
            target_left_open_gap_score=random.random()*(-10),
            target_left_extend_gap_score=random.random()*(-10),
            target_right_open_gap_score=random.random()*(-10),
            target_right_extend_gap_score=random.random()*(-10),
            query_internal_open_gap_score=random.random()*(-10),
            query_internal_extend_gap_score=random.random()*(-10),
            query_left_open_gap_score=random.random()*(-10),
            query_left_extend_gap_score=random.random()*(-10),
            query_right_open_gap_score=random.random()*(-10),
            query_right_extend_gap_score=random.random()*(-10)
        )

        return AlignerBuilder().build(args)

    def generate_population(self, population_size):
        return [self.generate_individual() for _ in range(population_size)]

    def select_best_individuals(self, population, num_individuals):
        return sorted(population, key=self.fitness_function, reverse=True)[:num_individuals]

    def run(self):
        population = self.generate_population(self.population_size)
        for _ in range(self.max_generations):
            new_population = []
            for _ in range(self.max_generations):
                parent1, parent2 = self.select_best_individuals(population, 2)
                child = self.crossover(parent1, parent2)
                child = self.mutate(child)
                new_population.append(child)
            population = new_population
        return self.select_best_individuals(population, 1)[0]