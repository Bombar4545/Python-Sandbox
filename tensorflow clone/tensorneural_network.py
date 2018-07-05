
class tensor(object):
    '''
        Immutable tensor object
    '''
    def __init__(self):
        self.dim = list()
        self.data = list()

class scalar(tensor):
    def __init__(self, val:float = 0.0):
        self.dim = []
        self.data = [float(val)]

    def __add__(self, value:tensor):
        if isinstance(value, scalar):
            return scalar(self.data[0] + value.data[0])
        else:
            return None

    def __sub__(self, value:tensor):
        if isinstance(value, scalar):
            return scalar(self.data[0] - value.data[0])
        else:
            return None
    
    def __mul__(self, value:tensor):
        if isinstance(value, scalar):
            return scalar(self.data[0] * value.data[0])
        else:
            return None
    
    def __div__(self, value:tensor):
        if isinstance(value, scalar):
            return scalar(self.data[0] / value.data[0])
        else:
            return None
    
    def __str__(self):
        return str(self.data[0]) + 'f'
    
    def __repr__(self):
        return 'scalar: ' + self.data[0] + 'f'
    
    def __len__(self):
        return 0
    
    def __eq__(self, other):
        if isinstance(other, scalar):
            return self.data[0] == other.data[0]
        else:
            return None
    
    def __ne__(self, other):
        return not self == other
    
    


class vector(tensor):
    '''
        Immutable rank 1 tenosor
    '''

class matrix(tensor):
    pass


a = scalar(3)
b = scalar(4)
print(a + b)