def parse_pdb_file(filepath):
    
    """
    Parses a PDB file; if the file is not in the current directory, one must provide the entire filepath.

    >>> parse_pdb_file('4d2i.pdb')
        [(),(Atom name, Amino Acid name, x-coordinate, y-coordinate, z-coordinate),()]
    """

    atom_list = []
    with open(filepath) as fp:
       for line in fp:
           words = line.strip().split()
           if words[0] == 'ATOM':
               atom_list.append((words[2], words[3], words[6], words[7], words[8]))
    return atom_list

if __name__ == '__main__':
   print(parse_pdb_file('4d2i.pdb'))
