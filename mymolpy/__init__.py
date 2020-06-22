"""
mymolpy
A Python package for analyzing and visualizing pdb and xyz files. For MolSSI May webinar series.
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_distance
from .molecule import build_bond_list, calculate_molecular_mass, calculate_center_of_mass
from .visualize import draw_molecule, bond_histogram
from .io import open_pdb, open_xyz, write_xyz

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
