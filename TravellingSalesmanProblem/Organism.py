class Organism:
    def __init__(self, cities):
        self.cities = cities
        self.road_length = None
        self.fitness = None

    def calculate_road_length(self):
        total_distance = 0

        for i in range(len(self.cities)):
            current_city = self.cities[i]
            next_city = self.cities[(i + 1) % len(self.cities)]

            distance = ((next_city[1] - current_city[1])**2 + (next_city[2] - current_city[2])**2)**0.5
            total_distance += distance

        self.road_length = total_distance

    def calculate_fitness(self, global_maximum):
        if self.road_length is None:
            self.calculate_road_length()

        self.fitness = -self.road_length + global_maximum