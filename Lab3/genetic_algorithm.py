import random
import tqdm
import numpy as np
from functions import bukin_2d


def set_seed(seed: int) -> None:
    # Set fixed random seed to make the results reproducible
    random.seed(seed)
    np.random.seed(seed)


class GeneticAlgorithm:
    def __init__(
            self,
            population_size: int,
            mutation_rate: float,
            mutation_strength: float,
            crossover_rate: float,
            num_generations: int,
    ):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.mutation_strength = mutation_strength
        self.crossover_rate = crossover_rate
        self.num_generations = num_generations

    def initialize_population(self) -> np.ndarray:
        # Initialize the population and return the result

        # Returns  random uniform distribution of values over [0,1).
        uni_population = np.random.rand(self.population_size, 2)

        # Re-scaling of the population from [0,1) to both [-15, -5] for x and [-3, 3] for y.
        scale_population = np.multiply(uni_population, [10, 6])
        new_population = np.add(scale_population, [-15, -3])
        return new_population

    def evaluate_population(self, population) -> np.ndarray:
        # Evaluate the fitness of the population and return the values for each individual in the population

        evaluation = [bukin_2d(val[0], val[1]) for val in population]
        return np.array(evaluation)

    def selection(self, population, fitness_values) -> np.ndarray:
        # Implement selection mechanism (Tournament Selection) and return the selected individuals.

        selected_individuals = np.empty(shape=(0, 2))
        for _ in range(self.population_size // 2):
            while True:
                first_contestant = np.random.randint(len(population))
                second_contestant = np.random.randint(len(population))
                if first_contestant != second_contestant:
                    break

            # Tournament selection:
            if fitness_values[first_contestant] <= fitness_values[second_contestant]:
                selected_individual = first_contestant
            else:
                selected_individual = second_contestant

            individual = population[selected_individual]
            selected_individuals = np.append(selected_individuals, [individual], axis=0)

            # population = np.delete(population, first_contestant, axis=0)
            # fitness_values = np.delete(fitness_values, first_contestant)
            #
            # population = np.delete(population, second_contestant, axis=0)
            # fitness_values = np.delete(fitness_values, second_contestant)

        return selected_individuals

    @staticmethod
    def rand_interpolation(alpha: float, parent1, parent2) -> np.ndarray:
        x = alpha * parent1[0] + (1 - alpha) * parent2[0]
        y = alpha * parent1[1] + (1 - alpha) * parent2[1]
        return np.array([x, y])

    def crossover(self, parents) -> np.ndarray:
        # Implement the crossover mechanism over the parents and return the offspring

        children = np.empty(shape=(0, 2))
        while len(children) < self.population_size:
            while True:
                first_parent = np.random.randint(len(parents))
                second_parent = np.random.randint(len(parents))
                if first_parent != second_parent:
                    break

            crossover = np.random.random(size=None)
            if crossover < self.crossover_rate:
                alpha = np.random.random(size=None)
                offspring1 = self.rand_interpolation(alpha, parents[first_parent], parents[second_parent])
                offspring2 = self.rand_interpolation(alpha, parents[second_parent], parents[first_parent])
            else:
                offspring1, offspring2 = parents[first_parent], parents[second_parent]

            children = np.append(children, [offspring1, offspring2], axis=0)

        return children

    def gaussian_op(self):
        return np.multiply(np.random.standard_normal(size=2), self.mutation_strength)

    def mutate(self, individuals: np.ndarray) -> np.ndarray:
        # Implement mutation mechanism over the given individuals and return the results

        for individual in individuals:
            if np.random.random() < self.mutation_rate:
                np.add(individual, self.gaussian_op(), out=individual)
                np.minimum(individual, np.array([-5, 3]), out=individual)
                np.maximum(individual, np.array([-15, -3]), out=individual)

        return individuals

    def evolve(self, seed: int) -> ...:
        # Run the genetic algorithm and return the lists that contain the best solution for each generation,
        #   the best fitness for each generation and average fitness for each generation
        set_seed(seed)

        population = self.initialize_population()

        best_solutions = []
        best_fitness_values = []
        average_fitness_values = []

        for generation in tqdm.tqdm(range(self.num_generations)):
            fitness_values = self.evaluate_population(population)
            best_fitness = np.min(fitness_values).tolist()
            average_fitness = np.mean(fitness_values).tolist()
            best_solution = population[np.where(fitness_values == best_fitness)[0][0]].tolist()

            parents_for_reproduction = self.selection(population, fitness_values)
            offspring = self.crossover(parents_for_reproduction)
            population = self.mutate(offspring)

            best_solutions.append(best_solution)
            best_fitness_values.append(best_fitness)
            average_fitness_values.append(average_fitness)

        return best_solutions, best_fitness_values, average_fitness_values
