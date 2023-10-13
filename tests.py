import pytest

from app import convert, kelvin_to_fahrenheit, kelvin_to_celsius, fahrenheit_to_kelvin, fahrenheit_to_celsius, celsius_to_kelvin, celsius_to_fahrenheit

def test_convert():
    assert convert("110k") == "110.0 K = -261.67 F\n110.0 K = -163.15 C"
    
def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32.00

def test_kelvin_to_celsius():
    assert round(kelvin_to_celsius(273.15), 2) == 0.00

def test_fahrenheit_to_kelvin():
    assert round(fahrenheit_to_kelvin(32.00), 2) == 273.15

def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(32.00), 2) == 0.00

def test_celsius_to_kelvin():
    assert round(celsius_to_kelvin(0.00), 2) == 273.15

def test_celsius_to_fahrenheit():
    assert round(celsius_to_fahrenheit(0.00), 2) == 32.00

