from Protein import Protein
class AminoAcid:

    def __init__(self, parent=Protein(), name="", id=0, atoms=[], N=(0, 0, 0), C_alpha=(0, 0, 0), C_dash=(0, 0, 0), coordinates=[], SS=""):
        self.parent = parent
        self.name = name
        self.id = id
        self.atoms = atoms
        self.N = N
        self.C_alpha = C_alpha
        self.C_dash = C_dash
        self.coordinates = coordinates
        self.SS = SS

    def find_parent(self, parent):
        return self.parent
    
    def find_name(self, name):
        return self.name
    
    def find_id(self, id):
        return self.id
    
    def find_atoms(self, atoms):
        return self.atoms
    
    def find_coordinates(self, coordinates):
        return self.coordinates
    
    def find_SS(self, SS):
        return self.SS

    