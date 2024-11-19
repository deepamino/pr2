import random
import copy

from processing.AlignerBuilder import *

seq1, seq2 = None, None

def fitness_function(aligner):
    global seq1, seq2
    print(aligner_args(aligner))
    print(aligner.align(seq1, seq2).score)
    return aligner.align(seq1, seq2).score

def crossover(parent1, parent2):
    child = copy.deepcopy(parent1)
    parent1_args = aligner_args(parent1)
    parent2_args = aligner_args(parent2)

    for key in parent1_args.__dict__:
        if random.random() < 0.5:
            setattr(child, key, getattr(parent2_args, key))

    return child
    
def aligner_args(aligner):
    return AlignerArgs(
        match_score=aligner.match_score,
        mismatch_score=aligner.mismatch_score,
        target_internal_open_gap_score=aligner.target_internal_open_gap_score,
        target_internal_extend_gap_score=aligner.target_internal_extend_gap_score,
        target_left_open_gap_score=aligner.target_left_open_gap_score,
        target_left_extend_gap_score=aligner.target_left_extend_gap_score,
        target_right_open_gap_score=aligner.target_right_open_gap_score,
        target_right_extend_gap_score=aligner.target_right_extend_gap_score,
        query_internal_open_gap_score=aligner.query_internal_open_gap_score,
        query_internal_extend_gap_score=aligner.query_internal_extend_gap_score,
        query_left_open_gap_score=aligner.query_left_open_gap_score,
        query_left_extend_gap_score=aligner.query_left_extend_gap_score,
        query_right_open_gap_score=aligner.query_right_open_gap_score,
        query_right_extend_gap_score=aligner.query_right_extend_gap_score,
    )
    

def mutate(individual):
    individual_args = aligner_args(individual)
    for key in individual_args.__dict__:
        if random.random() < 0.1:
            setattr(individual, key, random.random())
    return individual

def generate_individual():
    args = AlignerArgs(
        match_score=random.random()*10,
        mismatch_score=random.random()*(-10)
    )

    return AlignerBuilder().with_args(args).build()

def generate_population(population_size):
    return [generate_individual() for _ in range(population_size)]

def select_individuals(population, num_individuals):
    return random.sample(population, num_individuals)

def select_best_individuals(population, num_individuals):
    return sorted(population, key=fitness_function, reverse=True)[:num_individuals]

def genetic_algorithm(population_size, num_generations, sequence1, sequence2):
    global seq1, seq2
    seq1, seq2 = sequence1, sequence2

    population = generate_population(population_size)
    for _ in range(num_generations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_individuals(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
    return select_best_individuals(population, 1)[0]