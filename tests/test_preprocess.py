from src import preprocess

from numpy import testing as npt

def test_foo():
    npt.assert_almost_equal(3.0, preprocess.foo(1.0, 2))
