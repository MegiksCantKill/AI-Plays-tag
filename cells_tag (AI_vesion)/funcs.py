import random
import numpy as np
import json



def relu(x):
    return max(0, x)

def check_model(weights):
    seconds_survived = 0
    pos = np.array([random.randint(0, 80), random.randint(0, 80)])
    enemy = np.array([random.randint(0, 80), random.randint(0, 80)])    
    while pos[0] != enemy[0] and pos[1] != enemy[1]:
        seconds_survived += 1
        dir_ = np.maximum(0, np.dot([pos[0], pos[1], enemy[0], enemy[1]], weights[0]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], weights[1]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], weights[2]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], weights[3]))
        
        for i, _ in enumerate(dir_):
            if dir_[i] == 0:
                pos[i] -= 1
            if dir_[i] > 0:
                pos[i] += 1

        if enemy[0] > pos[0]:
            enemy[0] -= 1
        if enemy[0] < pos[0]:
            enemy[0] += 1
            
        if enemy[1] > pos[1]:
            enemy[1] -= 1
        if enemy[1] < pos[1]:
            enemy[1] += 1
	
        if enemy[0] > 80:
            break
        if enemy[0] < 0:
            break
        if enemy[1] > 80:
            break
        if enemy[1] < 0:
            break
		
        if pos[0] > 80:
            break
        if pos[0] < 0:
            break
        if pos[1] > 80:
            break
        if pos[1] < 0:
            break
	

        print(f"POS: {pos}")
        print(f"ENEMY: {enemy}")
            
    return seconds_survived
        

def mutate(weights, mutation_rate=0.1):
    new_weights = []
    for layer in weights:
        layer = np.array(layer)

        mutation = np.random.randn(*layer.shape) * mutation_rate
        new_layer = layer + mutation
        new_weights.append(new_layer)
    return new_weights
    
        
def genetic_algorithm(weights, generations=50, population_size=30, mutation_rate=0.1):
    best_weights = weights
    best_fitness = check_model(best_weights)

    for generation in range(generations):
        population = (mutate(best_weights, mutation_rate) for _ in range(population_size))
        
        best_in_population = None
        best_population_fitness = float('-inf')

        for candidate_weights in population:
            fitness = check_model(candidate_weights)
            
            if fitness > best_population_fitness:
                best_in_population = candidate_weights
                best_population_fitness = fitness
                print(f"New: {best_in_population}\nSteps survived: {best_population_fitness}\nStep: {generation + 1}")

        if best_population_fitness > best_fitness:
            best_weights = best_in_population
            best_fitness = best_population_fitness
        
        print(f"Generation {generation + 1}: Best fitness = {best_fitness}")

    return best_weights


def vector_avg(vectors_list):
    x_sum = 0
    y_sum = 0
    for vector in vectors_list:
        x_sum += vector[0]
        y_sum += vector[1]
    x_sum /= len(vectors_list)
    y_sum /= len(vectors_list)
    avg_vector = []
    avg_vector.append(x_sum)
    avg_vector.append(y_sum)
    return avg_vector
        

if __name__ == "__main__":
    ...
