
class AminoAcid:

    def __init__(self, parent, name, id, atoms, coordinates, SS):
        self.parent = parent
        self.name = name
        self.id = id
        self.atoms = atoms
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

    