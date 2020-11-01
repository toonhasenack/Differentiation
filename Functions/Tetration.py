import numpy as np
from math import log,e,floor,sin
import matplotlib.pyplot as plt

class Tower():
    
    """
    This is a class that stores a Power Tower. 
    You can:
     - Get the answer by calling the evaluate() method
     - Append a sequece of powers with the append() method
     - Power-up two Tower objects
     
    """
    
    def __init__(self, seq):
        self.seq = seq
        self.ans = self.evaluate()
    
    def append(self,ext_seq):
        self.seq = np.append(self.seq,ext_seq)

    def evaluate(self):
        rev_seq = np.flip(self.seq)
        temp_ans = rev_seq[0]
        for i in range(1,len(rev_seq)):
            temp_ans = rev_seq[i]**temp_ans
        ans = temp_ans    
        return ans
    
    def power(self,ext_Tower):
        new_Tower = self
        new_Tower.append(ext_Tower.seq)
        return new_Tower

class Tetrate(Tower): 
    
    """
    This class inherits the Tower() class.
    Additional features are:
     - 
    """
    
    def __init__(self, a, x):
        self.a = a
        self.x = x
        self.dec = self.x - floor(self.x)
        self.seq = np.zeros(floor(self.x)) + self.a
        self.value = self.evaluate()