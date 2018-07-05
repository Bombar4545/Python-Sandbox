import random as r
import math


def random(a:int=20, b:int=10):
    return r.random() * a - b

def randomList(lengh:int, a:int=20, b:int=10):
    return [random(a, b) for _ in range(lengh)]

class matrix(object):
    def __init__(self, row:int=1, col:int=1, init:str='zero', size:int=1):
        if init == 'zero':
            self.data = [0.0] * row * col
            self.row = row
            self.col = col
        elif init == 'random':
            self.data = randomList(row * col)
            self.row = row
            self.col = col
        elif init == 'one':
            self.data = [1.0] * row * col
            self.row = row
            self.col = col
        elif init == 'identity':
            self.data = [0.0] * size * size
            self.row, self.col = size, size

            for i in range(size):
                self.set(i, i, 1.0)
            
    def get(self, row, col):
        return 
    
    def set(self, row, col, val):
        self.data[row * self.col + col] = val
    
    def __len__(self):
        return self.row * self.col
    
    def __mul__(self, other):
        if isinstance(other, list):
            if len(other) == self.col:
                new = []
                for m in range(0, len(self), self.col):
                    vec = self.data[m:m + self.col]
                    new.append(sum([x * y for x,y in zip(other, vec)]))
                return new
            else:
                return None
        else:
            return None
    
    def randomize(self):
        for i in range(len(self)):
            self.data[i] = random()
    
    def __str__(self):
        s = 'matrix' + str((self.row, self.col)) + '\n'
        for m in range(0, len(self), self.col):
            s = s + str(self.data[m:m + self.col]) + '\n'
        return s

class neuralnet(object):
    def __init__(self, *layers:int, activation:str='tanh', minit:bool='one'): 
        self.weights = []
        self.layer_count = len(layers)
        self.layer_map = list(layers)
        self.biases = []

        for i in range(self.layer_count - 1):
            tmp = matrix(self.layer_map[i + 1], self.layer_map[i], init=minit)
            self.weights.append(tmp)

        for a in self.layer_map:
            self.biases.append(randomList(a))
        
        if activation == 'sigmoid':
            self.activation = lambda value : 1 / (1 + math.e ** (- value))
        elif activation == 'relu':
            self.activation = lambda value : 0 if value < 0 else value
        elif activation == 'tanh':
            self.activation = lambda value : math.tanh(value)
        else:
            self.activation = lambda value : value
    
    def run(self, vec:list, start:int=0, offset:int=0):
        if start >= self.layer_count - 1 - offset:
            return vec

        step_vec = self.weights[start] * vec
        step_vec = [self.activation(a + b) for a, b in zip(step_vec, self.biases[start + 1])]

        return self.run(step_vec, start + 1, offset)
    
    def randomize(self):
        for mat in self.weights:
            mat.randomize()
    
    def cost(self, input_vec:list, output_vec:list, input_offset:int=0, output_offset:int=0):
        result = self.run(input_vec, input_offset, output_offset)
        return sum([(a - b)**2 for a, b in zip(result, output_vec)])
        

if __name__ == '__main__':
    # m1 = matrix(init='identity', size=4)
    # print(m1 * [1, 2, 3, 4])

    # a basic neural net with activation function and bias
    # currently implementing backpropagation
    net = neuralnet(4, 10, 1, activation='tanh', minit='random')
    net.randomize() # randomizes weights

    print(net.run([1.0, 1.0, 1.0, 1.0]))

