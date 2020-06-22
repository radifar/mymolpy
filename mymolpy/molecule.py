"""
Miscelaneous function related to molecule
"""

from .measure import calculate_distance
from .atom_data import atomic_weights


def build_bond_list(coordinates, max_bond=1.5, min_bond=0):

    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    if min_bond < 0:
        raise ValueError("Invalid minimum bond distance entered! Minimum bond distance must be greater than zero!")

    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1 + 1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds


def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.
    
    Parameters
    ----------
    symbols : list
        A list of elements.
    
    Returns
    -------
    mass : float
        The mass of the molecule
    """
    
    mass = 0.0

    for symbol in symbols:
        atomic_mass = atomic_weights[symbol]
        mass += atomic_mass
    
    return mass
