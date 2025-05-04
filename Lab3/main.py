from genetic_algorithm import GeneticAlgorithm
import matplotlib.pyplot as plt


def plot_fitness_values(exp, fitness_values):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.plot(fitness_values)
    ax1.set_yscale('log')
    ax1.annotate(f'{fitness_values[0]:3.6f}', (0.0, fitness_values[0]))
    ax1.annotate(f'{fitness_values[-1]:3.6f}', (len(fitness_values), fitness_values[-1]))

    ax1.set_title(f"Best Fitness Values of Experiment: {exp}")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Best Fitness Value")
    fig1.show()


def plot_average_fitness_values(exp, avg_fitness_values):
    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    ax2.plot(avg_fitness_values)
    ax2.set_title(f"Average Fitness Values of Experiment: {exp}")
    ax2.set_yscale('log')
    ax2.annotate(f'{avg_fitness_values[0]:10.5f}', (0.0, avg_fitness_values[0]))
    ax2.annotate(f'{avg_fitness_values[-1]:10.5f}', (len(avg_fitness_values), avg_fitness_values[-1]))

    ax2.set_xlabel("Generation")
    ax2.set_ylabel("Average Fitness Value")
    fig2.show()


if __name__ == "__main__":
    # Experiment 1
    print("---- Experiment 1 ----")
    ga = GeneticAlgorithm(
        population_size=10000,
        mutation_rate=0.05,
        mutation_strength=6,
        crossover_rate=0.5,
        num_generations=150,
    )
    best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=5)
    plot_fitness_values(1, fitness_values)
    plot_average_fitness_values(1, avg_fitness_values)
    print("\nBest solution: ", best_solutions[-1])

    # print("* Seed 5: *")
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=5)
    # plot_fitness_values(5, fitness_values)
    # plot_average_fitness_values(5, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Seed 10101 *")
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=10101)
    # plot_fitness_values(10101, fitness_values)
    # plot_average_fitness_values(10101, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Seed 58496 *")
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=58496)
    # plot_fitness_values(58496, fitness_values)
    # plot_average_fitness_values(58496, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Seed 123456 *")
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=123456)
    # plot_fitness_values(123456, fitness_values)
    # plot_average_fitness_values(123456, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Seed 987654 *")
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=987654)
    # plot_fitness_values(987654, fitness_values)
    # plot_average_fitness_values(987654, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # Experiments relating to the population:
    # print("* Population 5000 *")
    # ga.population_size = 5000
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=5)
    # plot_fitness_values(5000, fitness_values)
    # plot_average_fitness_values(5000, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Population 2500 *")
    # ga.population_size = 2500
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=5)
    # plot_fitness_values(2500, fitness_values)
    # plot_average_fitness_values(2500, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Population 1000 *")
    # ga.population_size = 1000
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=5)
    # plot_fitness_values(1000, fitness_values)
    # plot_average_fitness_values(1000, avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # Experiments relating to the change of the crossover value:
    # ga.population_size = 10000
    # print("* Seed 456789 *")
    # print("* Crossover rate 0.1 *")
    # ga.crossover_rate = 0.1
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Crossover rate 0.1", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.1", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.25 *")
    # ga.crossover_rate = 0.25
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Crossover rate 0.25", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.25", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.5 *")
    # ga.crossover_rate = 0.5
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Crossover rate 0.5", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.5", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.75 *")
    # ga.crossover_rate = 0.75
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Crossover rate 0.75", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.75", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.9 *")
    # ga.crossover_rate = 0.9
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Crossover rate 0.9", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.9", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # print("* Seed 963852 *")
    # print("* Crossover rate 0.1 *")
    # ga.crossover_rate = 0.1
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Crossover rate 0.1", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.1", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.25 *")
    # ga.crossover_rate = 0.25
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Crossover rate 0.25", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.25", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.5 *")
    # ga.crossover_rate = 0.5
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Crossover rate 0.5", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.5", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.75 *")
    # ga.crossover_rate = 0.75
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Crossover rate 0.75", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.75", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Crossover rate 0.9 *")
    # ga.crossover_rate = 0.9
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Crossover rate 0.9", fitness_values)
    # plot_average_fitness_values("Crossover rate 0.9", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # Experiments concerning mutation rate and strength
    # print("* Seed 963852 *")
    # print("* Mutation rate 0.1 *")
    # ga.mutation_rate = 0.1
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Mutation rate 0.1", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.1", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation rate 0.05 *")
    # ga.mutation_rate = 0.05
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Mutation rate 0.05", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.05", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation rate 0.001 *")
    # ga.mutation_rate = 0.001
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=963852)
    # plot_fitness_values("Mutation rate 0.001", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.001", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # print("* Seed 789123 *")
    # print("* Mutation rate 0.1 *")
    # ga.mutation_rate = 0.1
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation rate 0.1", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.1", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation rate 0.05 *")
    # ga.mutation_rate = 0.05
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation rate 0.05", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.05", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation rate 0.001 *")
    # ga.mutation_rate = 0.001
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation rate 0.001", fitness_values)
    # plot_average_fitness_values("Mutation rate 0.001", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # Experiments done regarding the mutation strength.
    # print("* Seed 789123 *")
    # print("* Mutation strength 8 *")
    # ga.mutation_strength = 8
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation strength 8", fitness_values)
    # plot_average_fitness_values("Mutation rate 8", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation strength 2 *")
    # ga.mutation_strength = 2
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation strength 2", fitness_values)
    # plot_average_fitness_values("Mutation strength 2", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation strength 0.5 *")
    # ga.mutation_strength = 0.5
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=789123)
    # plot_fitness_values("Mutation strength 0.5", fitness_values)
    # plot_average_fitness_values("Mutation strength 0.5", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])

    # print("* Seed 456789 *")
    # print("* Mutation strength 8 *")
    # ga.mutation_strength = 8
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Mutation strength 8", fitness_values)
    # plot_average_fitness_values("Mutation strength 8", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation strength 2 *")
    # ga.mutation_strength = 2
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Mutation strength 2", fitness_values)
    # plot_average_fitness_values("Mutation strength 2", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
    #
    # print("* Mutation strength 0.5 *")
    # ga.mutation_strength = 0.5
    # best_solutions, fitness_values, avg_fitness_values = ga.evolve(seed=456789)
    # plot_fitness_values("Mutation strength 0.5", fitness_values)
    # plot_average_fitness_values("Mutation strength 0.5", avg_fitness_values)
    # print("\nBest solution: ", best_solutions[-1])
