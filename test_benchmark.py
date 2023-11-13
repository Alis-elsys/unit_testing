import pytest
from app import kelvin_to_fahrenheit
from flask import Flask

@pytest.mark.benchmark(group="kelvin_to_fahrenheit")
def test_kelvin_to_fahrenheit(benchmark):
    result = benchmark(kelvin_to_fahrenheit, 300) 
    assert isinstance(result, float)
