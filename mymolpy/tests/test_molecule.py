"""
Unit and regression test for the molecule module
"""

import mymolpy
import pytest
import numpy as np

def test_build_bond_list():

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])

    bonds = mymolpy.build_bond_list(coordinates)

    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_build_bond_failure():

    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])

    with pytest.raises(ValueError):
        bonds = mymolpy.build_bond_list(coordinates, min_bond=-1)


def test_build_bond_type_error():

    coordinates = [
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ]

    with pytest.raises(TypeError):
        bonds = mymolpy.build_bond_list(coordinates)


def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']

    calculated_mass = mymolpy.calculate_molecular_mass(symbols)

    actual_mass = 16.04

    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass

def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])

    center_of_mass = mymolpy.calculate_center_of_mass(symbols, coordinates)

    expected_center = np.array([1, 1, 1])

    assert True == np.array_equal(center_of_mass, expected_center)