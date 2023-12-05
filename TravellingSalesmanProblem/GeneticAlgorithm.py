from Population import Population
from Organism import Organism
import random

class GeneticAlgorithm:
    def __init__(self, cities, number_of_epochs, mutation_probability, population_size):
        self.population = Population(population_size, cities)
        self.number_of_epochs = number_of_epochs
        self.mutation_probability = mutation_probability
        self.fitness_per_epoch = []
        self.population_size = population_size

    def reproduction(self):
        fitness_values = [organism.fitness for organism in self.population.organisms]
        total_fitness = sum(fitness_values)
        probabilities = [fitness / total_fitness for fitness in fitness_values]

        new_population = []
        for _ in range(self.population_size):
            selected = random.choices(self.population.organisms, probabilities)[0]
            new_population.append(selected)

        self.population.population = new_population

    def crossover(self):
        new_population = []

        while len(self.population.organisms) >= 2:
            parent1 = random.choice(self.population.organisms)
            self.population.organisms.remove(parent1)
            parent2 = random.choice(self.population.organisms)
            self.population.organisms.remove(parent2)

            point1, point2 = sorted(random.sample(range(len(parent1.cities)-2), 2))

            while point1 == point2:
                point1, point2 = sorted(random.sample(range(len(parent1.cities)-2), 2))

            child1 = self.order_crossover(parent1, parent2, point1, point2, 1)
            child2 = self.order_crossover(parent2, parent1, point1, point2, 2)

            new_population.extend([child1, child2])

        if len(self.population.organisms) == 1:
            new_population.append(self.population.organisms[0])

        self.population.organisms = new_population

    def order_crossover(self, parent1, parent2, point1, point2, child_number):
        child_cities = [None] * len(parent1.cities)
        if child_number == 1:
            child_cities[point1+1:point2+1] = parent2.cities[point1+1:point2+1]
            remaining_cities = [city for city in parent1.cities if city not in child_cities]
        elif child_number == 2:
            child_cities[point1+1:point2+1] = parent1.cities[point1+1:point2+1]
            remaining_cities = [city for city in parent2.cities if city not in child_cities]

        # Fill the last part (from point2 to the end) with cities from remaining cities
        fill_index = point2 + 1
        for city in remaining_cities:
            child_cities[fill_index] = city
            fill_index = (fill_index + 1) % len(child_cities)

        child = Organism(child_cities)

        return child

    def mutation(self):
        for organism in self.population.organisms:
            random_number = random.random()

            if random_number <= self.mutation_probability:
                self.perform_mutation(organism)

    def perform_mutation(self, organism):
        index1, index2 = random.sample(range(len(organism.cities) - 1), 2)

        organism.cities[index1], organism.cities[index2] = organism.cities[index2], organism.cities[index1]

    def run_evolution(self):
        self.population.calculate_fitness()
        self.best_organism, self.worst_organism = self.population.get_best_and_worst_organisms()

        for epoch in range(self.number_of_epochs):
            self.reproduction()
            self.crossover()
            self.mutation()
            self.population.calculate_fitness()

            current_best, current_worst = self.population.get_best_and_worst_organisms()

            if current_best.fitness > self.best_organism.fitness:
                self.best_organism = current_best

            if current_worst.fitness < self.worst_organism.fitness:
                self.worst_organism = current_worst

            fitness_info = {
                "epoch": epoch + 1,
                "minimum_fitness": self.population.min_fitness,
                "maximum_fitness": self.population.max_fitness,
                "average_fitness": self.population.avg_fitness
            }
            self.fitness_per_epoch.append(fitness_info)