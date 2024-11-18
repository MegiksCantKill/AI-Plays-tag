import funcs
import json
import random
import numpy as np

not_trained_weights_file = json.load(open("weights.json", "r", encoding="utf-8"))
not_trained_weights_ = not_trained_weights_file["weights"]

class AI:
    def __init__(self, lr: float, weights: list, steps_of_training: int):
        self.lr = lr
        self.weights = weights
        self.steps = steps_of_training
    
    def train(self):
        for i1, layer in enumerate(self.weights):
            for i2, neuron in enumerate(layer):
                for i3, weight in enumerate(neuron):
                    weight += random.random()
        self.weights = funcs.genetic_algorithm(self.weights, self.steps, 100, self.lr)
        
      
        
    def predict(self, pos1, pos2, en1, en2):
        current_pos = [pos1, pos2]
        dir_ = np.maximum(0, np.dot([current_pos[0], current_pos[1], en1, en2], self.weights[0]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], self.weights[1]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], self.weights[2]))
        dir_ = np.maximum(0, np.dot([dir_[0], dir_[1], dir_[2], dir_[3]], self.weights[3]))
        
        
        for i, _ in enumerate(dir_):
            if dir_[i] > 0:
                current_pos[i] += 1
            if dir_[i] == 0:
                current_pos[i] -= 1
                
        return current_pos

        
    

    
if __name__ == "__main__":
    ai = AI(0.1, not_trained_weights_, 200)
    ai.train()
    print(ai.weights)
    not_trained_weights_file["weights"] = ai.weights
    weights_as_lists = [array.tolist() for array in not_trained_weights_file["weights"]]
    not_trained_weights_file["weights"] = weights_as_lists
    print(not_trained_weights_file)
    json.dump(dict(not_trained_weights_file), open("weights.json", "wt", encoding = "utf-8"), indent = 8)
