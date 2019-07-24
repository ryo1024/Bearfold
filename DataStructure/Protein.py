import numpy as np

class Protein:

    def __init__ (self, name:str="", aminoacids:list=[], lenseq:int=0):
        self.name = name
        self.aminoacids = aminoacids
        self.lenseq = lenseq
    
    def find(self, id):
        return self.aminoacids[id]

    