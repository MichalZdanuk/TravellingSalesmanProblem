from GeneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

cities_list = [
    ('A', 2, 2), ('B', 9, 8), ('C', 6, 6), ('D', 1, 8), ('E', 3, 7),
    ('F', 5, 7), ('G', 4, 3), ('H', 10, 5), ('I', 7, 4), ('J', 8, 1)
]

def plot_map(cities, title, position):
    plt.subplot(1, 2, position)
    plt.title(title)
    plt.xlim(-0.5, 10.5)
    plt.ylim(-0.5, 10.5)

    # Plot cities
    for city in cities:
        plt.scatter(city[1], city[2], c='red', marker='o')
        plt.text(city[1], city[2], city[0])

    # Connect cities in order
    for i in range(len(cities)):
        current_city = cities[i]
        next_city = cities[(i + 1) % len(cities)]
        plt.plot([current_city[1], next_city[1]], [current_city[2], next_city[2]], 'b-')

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)


number_of_epochs = 100
mutation_probability = 0.02
population_size = 16

tsp_instance = GeneticAlgorithm(cities_list, number_of_epochs, mutation_probability, population_size)
tsp_instance.run_evolution()

best_organism = tsp_instance.best_organism
worst_organism = tsp_instance.worst_organism

print(f"Best Organism: {best_organism.cities}, Fitness: {best_organism.fitness}, Road Length: {best_organism.road_length}")
print(f"Worst Organism: {worst_organism.cities}, Fitness: {worst_organism.fitness}, Road Length: {worst_organism.road_length}")

plt.figure(figsize=(10, 5))

plot_map(best_organism.cities, 'Best Organism', 1)
plot_map(worst_organism.cities, 'Worst Organism', 2)
plt.show()

# Fitness function plot
plt.plot([epoch_info['epoch'] for epoch_info in tsp_instance.fitness_per_epoch],
         [epoch_info['minimum_fitness'] for epoch_info in tsp_instance.fitness_per_epoch], label='Minimum Fitness')
plt.plot([epoch_info['epoch'] for epoch_info in tsp_instance.fitness_per_epoch],
         [epoch_info['average_fitness'] for epoch_info in tsp_instance.fitness_per_epoch], label='Average Fitness')
plt.plot([epoch_info['epoch'] for epoch_info in tsp_instance.fitness_per_epoch],
         [epoch_info['maximum_fitness'] for epoch_info in tsp_instance.fitness_per_epoch], label='Maximum Fitness')
plt.xlabel('Epochs')
plt.ylabel('Fitness')
plt.title('Fitness Function Across Epochs')
plt.legend()

plt.show()