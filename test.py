import pytest
import funcm1 as mult

class TestMultiplos:
    def setup(self):
        pass

    def test_multipol_5_7(self):
        result1 = mult.mutiplos(35)
        assert result1 == "fizzbuzz"

    def test_multipol_5(self):
        result2 = mult.mutiplos(5)
        assert result2 == "fizz"

    def test_multipol_7(self):
        result3 = mult.mutiplos(7)
        assert result3 == "buzz"
    