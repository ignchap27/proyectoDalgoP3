from pyeasyga import pyeasyga
import random
import numpy as np
import matplotlib.pyplot as plt


def pancake_Sort(representacion):
    #Inicializamos nuestra instancia de pyeasyga
    ga = pyeasyga.GeneticAlgorithm(representacion,
                                population_size=100,
                                generations=500,
                                crossover_probability=0.8,
                                mutation_probability=0.2,
                                elitism=True,
                                maximise_fitness=False)

        
    #Funcion que crea individuos, para la creacion de la población inicial
    def create_individual(data):
        individual = data[:]
        random.shuffle(individual)
        return individual

    #Una vez la creamos la asignamos a nuestra instancia de ga.
    ga.create_individual = create_individual

    # Ahora definimos nuestra función de crossover
    def crossover(parent_1, parent_2):
        crossover_index = random.randrange(1, len(parent_1))
        child_1a = parent_1[:crossover_index]
        child_1b = [i for i in parent_2 if i not in child_1a]
        child_1 = child_1a + child_1b

        child_2a = parent_2[crossover_index:]
        child_2b = [i for i in parent_1 if i not in child_2a]
        child_2 = child_2a + child_2b

        return child_1, child_2

    #Una vez la creamos la asignamos a nuestra instancia ga.
    ga.crossover_function = crossover

    def mutate(individual):
        mutate_index1 = random.randrange(len(individual))
        mutate_index2 = random.randrange(len(individual))
        individual[mutate_index1], individual[mutate_index2] = individual[mutate_index2], individual[mutate_index1]

    #Una vez la creamos la asignamos a nuestra instancia ga.
    ga.mutate_function = mutate

    def selection(population):
        # En el taller ustedes deben implementar una selección mas inteligente (ruleta)
        probabilities = []
        for i in population:
            #Invertimos el fitness para que los individuos con menor fitness tengan 
            # mayor probabilidad de ser seleccionados. Y sumamos 1 para evitar dividir entre 0
            probabilities.append((1/(i.fitness+1))) 
        
        total_prob = sum(probabilities)
        
        probabilities = [i/total_prob for i in probabilities] #normalizamos las probabilidades
        
        spin = random.random()
        current = 0
        
        for i in range(len(population)):
            current += probabilities[i]
            if current > spin:
                return population[i]

    #Una vez la creamos la asignamos a nuestra instancia ga.
    ga.selection_function = selection

    # Función de fitness: probablemente la mas importante
    def fitness (individual, data):
        collisions = 0
        for item in individual:
            item_index = individual.index(item)
            for elem in individual:
                elem_index = individual.index(elem)
                if item_index != elem_index:
                    if item - (elem_index - item_index) == elem or (elem_index - item_index) + item == elem:
                        collisions += 1
        return collisions

    #Una vez la creamos la asignamos a nuestra instancia ga.
    ga.fitness_function = fitness       # set the GA's fitness function

    #Primera generación
    ga.create_first_generation()

    def datos_generacion():
        fitness_po = [i.fitness for i in ga.current_generation]
        average = sum(fitness_po)/len(fitness_po)
        print("Fitness promedio:{} ".format(average))
        print("Mejor Individuo: {}".format(ga.best_individual()))
        
        return average, ga.best_individual()

    best_individual_fitness_history = []
    avg_fitness_history = []

    #Ahora generemos las siguientes N generaciones
    for i in range(1, 500+1):
        print("Generacion #{}".format(i))
        ga.create_next_generation()
        average, best_individual = datos_generacion()
        
        avg_fitness_history.append(average)
        best_individual_fitness_history.append(best_individual[0])
        
    #Para correr todas las generaciones definidas en la inicialización de ga.
    ga.run()
    ga.best_individual()
    
    return best_individual_fitness_history, avg_fitness_history
    
    
#n_queens = input("Ingrese el número de reinas: ")

# # representacion = [i for i in range(1, int(n_queens)+1)]

representacion = [1, 4, 3, 2, 5]
    
best_individual_fitness, avg_fitness = pancake_Sort(representacion)

print("Fitness promedio por generación: ", avg_fitness)
print("Mejor fitness por generación: ", best_individual_fitness)

plt.figure(figsize=(10, 5))
plt.plot(avg_fitness, label='Average Fitness')
plt.plot(best_individual_fitness, label='Best Individual Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')   
plt.title('Evolution of Avg Fitness With population size: {}'.format(population_size))
plt.legend()
plt.show()
