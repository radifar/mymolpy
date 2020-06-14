"""
Unit and regression test for the mymolpy package.
"""

# Import package, test suite, and other packages as needed
import mymolpy
import pytest
import sys

def test_mymolpy_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mymolpy" in sys.modules
