from Organism import Organism
import random

class Population:
    def __init__(self, population_size, cities):
        self.organisms = [Organism(random.sample(cities, len(cities))) for _ in range(population_size)]
        self.global_maximum = 0

    def calculate_road_lengths(self):
        for organism in self.organisms:
            organism.calculate_road_length()

    def calculate_fitness(self):
        self.calculate_road_lengths()
        self.update_global_maximum()

        for organism in self.organisms:
            organism.calculate_fitness(self.global_maximum)

        fitness_values = [organism.fitness for organism in self.organisms]
        self.min_fitness = min(fitness_values)
        self.max_fitness = max(fitness_values)
        self.avg_fitness = sum(fitness_values) / len(fitness_values)

    def update_global_maximum(self):
        current_maximum = max(self.organisms, key=lambda x: x.road_length).road_length
        self.global_maximum = max(self.global_maximum, current_maximum)

    def get_best_and_worst_organisms(self):
        return max(self.organisms, key=lambda x: x.fitness), min(self.organisms, key=lambda x: x.fitness)