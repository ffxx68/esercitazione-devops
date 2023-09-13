import pytest
from operazioni import *

def test_somma():
    assert somma(3, 5) == 8

def test_divis():
    with pytest.raises(Exception):
        res = divis(5, 0)